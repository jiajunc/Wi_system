# 🏬 Willhelm International Medication System

## Description

An easy appointment website designed for Willhelm International. Tool used: Django, Sqlite, Bootstrap, jQuery.

**Webiste:** [Deployed on Pythonanywhere](http://jasonchan.pythonanywhere.com)

## Admin view:

Administrator can be created only through terminal of server by using "./manage.py createsuperuser" command. An [administrator](http://jasonchan.pythonanywhere.com/admin)(username: test, password: test) has been created, please feel free to test the data intergrity and consistency.

1. Administrator has CRUD control of the user.
2. Administrator has CRUD control of the appointment.
3. Administrator has CRUD control of the prescription.
 
## Doctor view
 
1. Prescribe medication (type of medication/dosage/duration). (Doctor can only prescribe to those who have appointment in the future.)
2. view scheduled appointments
3. see patient appointment and medication history


## Patient View

1. book appointments with specific doctors - view only current medication and dosage.
