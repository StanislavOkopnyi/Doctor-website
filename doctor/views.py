from datetime import datetime
from django.forms.renderers import get_template
from django.http import HttpResponseRedirect
from django.template.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email_adress = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject=f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email_adress],
        )
        email.send()

        return HttpResponse("Email sent successfully")


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        answer = request.POST.get("answer")

        appointment = Appointment.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            answer=answer,
        )
        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Your request was saved successfully. Thanks {first_name} {last_name} for making appointment!")

        return HttpResponseRedirect(request.path)


class ManageAppointmentListView(ListView):
    template_name = "manage-appointments.html"
    login_required = True
    paginate_by = 3
    model = Appointment

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.now()
        appointment.save()

        data = {
            "first_name": appointment.first_name,
            "date": date,
        }
        message = get_template("email.html").render(data)
        email = EmailMessage(
            "About your appointment.",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email]
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS,
                             f"{date}")

        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
