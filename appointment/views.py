from users.models import CustomUser
from django.shortcuts import render, get_object_or_404
from .forms import PrescribeForm, AppointmentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required()
def make_appointment(request):
    patient = request.user
    if not patient.is_patient:
        return render(request, 'login.html', {})
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.app_patient = patient
            appointment.save()
            return redirect('patient_view_url')
    else:
        form = AppointmentForm
    return render(request, 'appointment/appointment_form.html', {'form': form})


@login_required()
def prescribe_to(request, pk):
    doctor = request.user
    if not doctor.is_doctor:
        return render(request, 'login.html', {})
    patient = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = PrescribeForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.pre_patient = patient
            prescription.pre_doctor = doctor
            prescription.save()
            return redirect('doctor_view_url')
    else:
        form = PrescribeForm
    return render(request, 'prescription/prescription_form.html', {'form':form})

