from django.db import models

# Create your models here.
class Service(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Duration = models.TimeField()
    
    def __str__(self):
        return self.Name
#just add 20.01
class Booking(models.Model):
    staff = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.CharField(max_length=10, blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.service} with {self.staff} on {self.date}"

class Staff(models.Model):
    staff_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=15)
    birthdate = models.DateField()
    status = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return self.name

