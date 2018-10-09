# Generated by Django 2.0.5 on 2018-10-06 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('dosage', models.CharField(max_length=20)),
                ('drug_name', models.CharField(max_length=20)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prescriptions', to='appointment.Appointment')),
            ],
        ),
    ]
