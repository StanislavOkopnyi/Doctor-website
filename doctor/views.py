from django.http import HttpResponseRedirect
from django.template.response import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


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

        messages.add_message(request, messages.SUCCESS,
                             "Your request was saved successfully")
        return HttpResponseRedirect(request.path)
