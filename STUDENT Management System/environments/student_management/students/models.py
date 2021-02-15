from django.db import models


#create models
class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    semester = models.CharField("Semester", max_length=3)
    phone = models.CharField(max_length=11)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name