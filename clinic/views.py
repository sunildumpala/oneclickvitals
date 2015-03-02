from django.shortcuts import render
from django.utils import timezone
from .models import Appointment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('appointment_date')
    return render(request, 'clinic/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'clinic/appointment_detail.html', {'appointment': appointment})

def appointment_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.author = request.user
            appointment.save()
            return redirect('clinic.views.appointment_detail', pk=appointment.pk)
    else:
        form = PostForm()
    return render(request, 'clinic/appointment_edit.html', {'form': form})

def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.author = request.user
            appointment.save()
            return redirect('clinic.views.appointment_detail', pk=appointment.pk)
    else:
        form = PostForm(instance=appointment)
    return render(request, 'clinic/appointment_edit.html', {'form': form})
