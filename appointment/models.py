from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator
from django.forms import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

User = get_user_model()
#
# class Doctor(models.Model):
#     doctor_ssn = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     specialty = models.CharField(max_length=20)
#
#     def __str__(self):
#         return '{} {}'.format(self.specialty, self.short_name)
#
#     @property
#     def short_name(self):
#         return '{} {}'.format(self.last_name.title(), self.first_name[0].upper())
#
#
# class Patient(models.Model):
#     patient_ssn = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return '{}'.format(self.short_name)
#
#     @property
#     def short_name(self):
#         return '{} {}'.format(self.last_name.title(), self.first_name[0].upper())

#
class Appointment(models.Model):
    class Meta:
        ordering = ['app_doctor', 'date', 'timeslot']
        unique_together = (('app_doctor', 'date', 'timeslot'),)

    TIMESLOT_LIST = (
        (0, '09:00 – 10:00'),
        (1, '10:00 – 11:00'),
        (2, '11:00 – 12:00'),
        (3, '12:00 – 13:00'),
        (4, '13:00 – 14:00'),
        (5, '14:00 – 15:00'),
        (6, '15:00 – 16:00'),
        (7, '16:00 – 17:00'),
        (8, '17:00 – 18:00'),
    )


    appointment_id = models.AutoField(primary_key=True)
    app_doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.PROTECT, default=1)
    app_patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.PROTECT, default=1)
    date = models.DateField()
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)

    def __str__(self):
        return '{} {}. Doctor: {}. Patient: {}.'.format(self.date, self.time, self.app_doctor, self.app_patient)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

    def patient_view(self):
        return '{} {}. Doctor: {}'.format(self.date, self.time, self.app_doctor)

    def doctor_view(self):
        return '{} {}. Patient: {}'.format(self.date, self.time, self.app_patient)


class Prescription(models.Model):

    DOSSAGE_LIST = (
        (0, '200mg'),
        (1, '400mg'),
        (2, '600mg'),
        (3, '800mg'),
        (4, '1g'),
        (5, '1 tablet'),
        (6, '2 tablets'),
        (7, '3 tablets'),
        (8, '4 tablets'),
    )

    FREQUENCY_LIST = (
        (0, 'Twice A Day'),
        (1, 'Once A Day'),
        (2, 'Once In Two Days'),
        (3, 'Once A Week'),
        (4, 'Twice A Week'),
        (5, 'Once A Month'),
        (6, 'Twice A Month'),
    )

    DRUG_LIST = (
        (0, 'Famotidine'),
        (1, 'Ranitidine'),
        (2, 'Esomeprazole'),
        (3, 'Aspirin'),
        (4, 'Ibuprofen'),
        (5, 'Diphenhydramine Hydrochloride'),
        (6, 'Hydroxyzine'),
        (7, 'Cetirizine Hydrochloride'),
        (8, 'Amoxicillin'),
    )

    prescription_id = models.AutoField(primary_key=True)
    pre_doctor = models.ForeignKey(User, related_name='doctor_prescriptions', on_delete=models.PROTECT, default=1)
    pre_patient = models.ForeignKey(User, related_name='patient_prescriptions', on_delete=models.PROTECT, default=1)
    dossage = models.IntegerField(choices=DOSSAGE_LIST, default=0)
    frequency = models.IntegerField(choices=FREQUENCY_LIST, default=0)
    drug = models.IntegerField(choices=DRUG_LIST, default=0)
    start_date = models.DateField(default= timezone.now)
    end_date = models.DateField(default= timezone.now)

    def __str__(self):
        return 'Drug: {}. Dossage: {}. Frequency: {}. Until:{}.'.format(self.drugMark, self.dossageMark, self.frequencyMark, self.end_date)

    @property
    def drugMark(self):
        return self.DRUG_LIST[self.drug][1]

    @property
    def dossageMark(self):
        return self.DOSSAGE_LIST[self.dossage][1]

    @property
    def frequencyMark(self):
        return self.FREQUENCY_LIST[self.frequency][1]

    class Meta:
        ordering = ['start_date', 'end_date']


