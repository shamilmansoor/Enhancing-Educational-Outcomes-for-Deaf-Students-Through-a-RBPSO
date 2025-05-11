from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    ADDRESS_CHOICES = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
    ]
    HEARING_LOSS_CHOICES = [
        ('Severe', 'Severe'),
        ('Moderate', 'Moderate'),
        ('Mild', 'Mild'),
    ]
    STUDY_TIME_CHOICES = [
        ('<1hr', '<1hr'),
        ('1-2hr', '1-2hr'),
        ('2-5hr', '2-5hr'),
        ('>5hr', '>5hr'),
    ]
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    address = models.CharField(max_length=10, choices=ADDRESS_CHOICES)
    hearing_loss = models.CharField(max_length=10, choices=HEARING_LOSS_CHOICES)
    school_support = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    paid_classes = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    ia1 = models.FloatField()
    ia2 = models.FloatField()
    ia3 = models.FloatField()
    nursery_attendance = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    internet_access = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    study_time = models.CharField(max_length=10, choices=STUDY_TIME_CHOICES)
    extracurricular = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    absences = models.IntegerField()
    predicted_marks = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True, default='')

    def __str__(self):
        return self.name
