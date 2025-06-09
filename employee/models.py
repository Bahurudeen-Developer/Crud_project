from django.db import models

# Create your models here.

class employee(models.Model):
    Employee_id  = models.CharField(max_length=30)
    Employee_name  = models.CharField(max_length=100)
    Employee_Emailid  = models.EmailField()
    Employee_contact = models.CharField(max_length=20)


    def __str__(self):
        return self.Employee_name
    
