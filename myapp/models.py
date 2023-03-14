from django.db import models
2
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=19, null=True)
    subject = models.CharField(max_length=20, null=True)
    exist = models.CharField(max_length=5, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
