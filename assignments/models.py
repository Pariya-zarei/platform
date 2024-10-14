from django.db import models
from courses.models import Course
from accounts.models import CustomUser

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submissions')
    submission_file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"Submission for {self.assignment.title} by {self.student.username}"
    