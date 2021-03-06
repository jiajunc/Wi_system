from datetime import date
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .forms import CustomUserCreationForm
from .models import CustomUser


# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        # isdoctor = request.POST['is_doctor']
        # if isdoctor == 'True':
        #     is_doctor = True
        # elif isdoctor == 'False':
        #     is_patient = True
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #generate patient view or user view according to login
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {})


def register_user(request):
    logout(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            second_name = form.cleaned_data.get('second_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            is_doctor = form.cleaned_data.get('is_doctor')
            is_patient = form.cleaned_data.get('is_patient')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


class DoctorView(LoginRequiredMixin, View):

    def get(self, request):
        user = doctor = request.user
        # only doctor user can view
        if not doctor.is_doctor:
            return render(request, 'login.html', {})
        today = date.today()
        appointment_list = doctor.doctor_appointments.all()
        return render_to_response(
            'doctor_view.html',
            {'today': today,
             'doctor': doctor,
             'user': user,
             'appointment_list': appointment_list}
        )


class PatientView(LoginRequiredMixin, View):

    def get(self, request):

        user = patient = request.user
        # only doctor user can view
        if not patient.is_patient:
            return render(request, 'login.html', {})
        today = date.today()
        prescription_list = patient.patient_prescriptions.all()
        appointment_list = patient.patient_appointments.all()
        return render_to_response(
            'patient_view.html',
            {'today': today,
             'patient': patient,
             'user': user,
             'prescription_list': prescription_list,
             'appointment_list': appointment_list}
        )


class PatientDetail(LoginRequiredMixin, View):

    def get(self, request, pk):
        user = doctor = request.user
        # only doctor user can view
        if not doctor.is_doctor:
            return render(request, 'login.html', {})
        patient = get_object_or_404(
            CustomUser,
            pk=pk
        )
        prescription_list = patient.patient_prescriptions.all()
        appointment_list = patient.patient_appointments.all()
        return render_to_response(
            'patient_detail.html',
            {'patient': patient,
             'doctor': doctor,
             'user': user,
             'prescription_list': prescription_list,
             'appointment_list': appointment_list}
        )
