from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    location = models.CharField(max_length=250)
    
    def _str_(self):
        return self.name