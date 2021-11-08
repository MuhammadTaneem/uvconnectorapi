from django.db import models


# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=255, null=False)
    student_id = models.CharField(max_length=15, unique=True, null=False)
    nick_name = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=15, null=True)
    birth_day = models.CharField(max_length=12, null=True)
    image = models.ImageField(upload_to='images/', default='images/logo.png')
    blood_group = models.CharField(max_length=12, null=True)
    blood_doner = models.BooleanField(null=True, default=False)
    REQUIRED_FIELDS = ['full_name', 'student_id']

    def __str__(self):
        if self.full_name:
            return self.full_name
