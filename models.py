from django.db import models

class formInfo(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')

    class Meta:
        db_table='testtable'

class loginfrom(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='login'


# class EmergencyContact(models.Model):
#     # location = models.CharField(max_length=100)
#     # hospital = models.CharField(max_length=100)
#     patient_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     emergency = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     contact_name = models.CharField(max_length=100)
#     relationship = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     home_address = models.TextField()
#     ambulance_service = models.BooleanField(default=False)
#     pickup_address = models.TextField()
#
#     class Meta():
#         db_table="emergencycontact"
