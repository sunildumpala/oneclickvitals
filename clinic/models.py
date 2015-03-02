from django.db import models
from django.utils import timezone
# Create your models here.

class Appointment(models.Model):
    author = models.ForeignKey('auth.User')
    patient_name = models.CharField(max_length=200)
    reason = models.TextField()
    appointment_date = models.DateTimeField(blank=True, null=True)

    def book_appointment(self):
        self.appointment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.patient_name
