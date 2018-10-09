from datetime import date
from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.views import View

from .models import Patient, Doctor, Appointment, Prescription
from django.shortcuts import render, get_object_or_404
from .forms import AppointmentForm, PrescriptionForm, PrescribeForm
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
# Create your views here.


def make_appointment(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            # return redirect('patient_detail', pk=patient.patient_ssn)
    else:
        form = AppointmentForm
    return render(request, 'appointment/appointment_form.html', {'form':form})


def make_prescription(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = doctor
            prescription.save()
            # return redirect('patient_detail', pk=patient.patient_ssn)
    else:
        form = PrescriptionForm
    return render(request, 'appointment/prescription_form.html', {'form':form})


# same prescriptionForm//pass the doctorpk by user pk
def prescribe(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PrescribeForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = doctor
            prescription.patient = patient
            prescription.save()
            # return redirect('patient_detail', pk=patient.patient_ssn)
    else:
        form = PrescribeForm
    return render(request, 'appointment/prescription_form.html', {'form':form})


class patient_detail(View):

    def get(self, request, docpk, patpk):
        patient = get_object_or_404(
            Patient,
            pk=patpk
        )
        today = date.today()
        prescription_list = patient.prescriptions.all()
        return render_to_response(
            'appointment/patient_detail.html',
            {'today': today,
             'docpk': docpk,
             'patient': patient,
             'prescription_list': prescription_list}
        )


class doctor_detail(View):

    def get(self, request, pk):
        doctor = get_object_or_404(
            Doctor,
            pk=pk
        )
        today = date.today()
        appointment_list = doctor.appointments.all()
        return render_to_response(
            'appointment/doctor_detail.html',
            {'today': today,
             'doctor': doctor,
             'appointment_list': appointment_list}
        )


class patient_view(View):

    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk
        )
        prescription_list = patient.prescriptions.all()
        appointment_list = patient.appointments.all()
        return render_to_response(
            'appointment/patient_view.html',
            {'patient': patient,
             'prescription_list': prescription_list,
             'appointment_list': appointment_list}
        )
