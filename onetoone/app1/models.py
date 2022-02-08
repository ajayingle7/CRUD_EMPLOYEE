from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Emp(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mno = PhoneNumberField()

    def __str__(self):
        return f'{self.eid}--{self.name}--{self.email}--{self.mno}'


class Role(models.Model):
    emp = models.OneToOneField(Emp,on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.emp}--{self.role}'


