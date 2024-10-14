from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Assignment
from courses.models import Course

@receiver(post_save, sender=Assignment)
def notify_students_on_assignment_update(sender, instance, created, **kwargs):
    course = instance.course
    subject = f"New Update in Assignment: {instance.title}"

    if created:
        message = f"A new assignment has been created in your course {course.name}."
    else:
        message = f"The assignment {instance.title} has been updated in your course {course.name}."

    recipients = [student.email for student in course.student_set.all()]  # Assuming you have a related field for students in the Course model

    send_mail(
        subject,
        message,
        'from@example.com',  # Replace with your "from" email
        recipients,
        fail_silently=False,
    )
