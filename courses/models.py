from django.db import models
from accounts.models import CustomUser  # فرض بر این است که مدل کاربر شما در accounts.models قرار دارد

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField(CustomUser, related_name='enrolled_courses', blank=True)  # اضافه کردن فیلد students

    def __str__(self):
        return self.name
