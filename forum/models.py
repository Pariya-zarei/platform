from django.db import models
from courses.models import Course
from accounts.models import CustomUser

class Post(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
