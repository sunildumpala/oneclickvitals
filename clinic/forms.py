from django import forms
from datetimewidget.widgets import DateTimeWidget
from .models import Appointment

class PostForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('patient_name', 'reason','appointment_date')
