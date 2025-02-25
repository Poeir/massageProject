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