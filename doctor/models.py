from django.db import models

# Create your models here.


class Appointment(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    answer = models.TextField()
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_dat = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
