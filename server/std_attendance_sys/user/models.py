from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    index_num = models.IntegerField()
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.index_num

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=50, verbose_name='email')
    
    def __str__(self):
        print(Lecturer._meta.get_fields())
        return f"{self.user.first_name} {self.user.last_name}"
