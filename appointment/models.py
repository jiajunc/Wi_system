from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone


class Doctor(models.Model):
    doctor_ssn = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.specialty, self.short_name)

    @property
    def short_name(self):
        return '{} {}'.format(self.last_name.title(), self.first_name[0].upper())


class Patient(models.Model):
    patient_ssn = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.short_name)

    @property
    def short_name(self):
        return '{} {}'.format(self.last_name.title(), self.first_name[0].upper())


class Appointment(models.Model):
    class Meta:
        unique_together = (('patient', 'doctor', 'date', 'timeslot'),'')
        ordering = ['date', 'timeslot']

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
    doctor = models.ForeignKey('Doctor', related_name='appointments', on_delete=models.PROTECT)
    patient = models.ForeignKey('Patient',  related_name='appointments', on_delete=models.PROTECT)
    date = models.DateField()
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]


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
    doctor = models.ForeignKey('Doctor', related_name='prescriptions', on_delete=models.PROTECT, default=000000000)
    patient = models.ForeignKey('Patient', related_name='prescriptions', on_delete=models.PROTECT, default=000000000)
    dossage = models.IntegerField(choices=DOSSAGE_LIST, default=10)
    frequency = models.IntegerField(choices=FREQUENCY_LIST, default=10)
    drug = models.IntegerField(choices=DRUG_LIST, default=10)
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
