from django.db import models

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    DEPARTMENT_CHOICES = [
        ('Physiotherapy', 'Physiotherapy'),
        ('Physical Health', 'Physical Health'),
        ('Treatments', 'Treatments'),
    ]

    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date = models.DateField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.department} on {self.date}"