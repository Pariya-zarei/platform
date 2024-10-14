from rest_framework import viewsets
from .models import Assignment
from .serializers import AssignmentSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Assignment, Submission


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


@login_required
def student_activity(request):
    student = request.user  # فرض بر این است که کاربر از نوع CustomUser است
    submissions = Submission.objects.filter(student=student)
    
    # برای هر تمرین، اطلاعات مربوط به تمرین را دریافت کنید
    activities = []
    for submission in submissions:
        activities.append({
            'assignment': submission.assignment,
            'grade': submission.grade,
            'submitted_at': submission.submitted_at,
        })
    
    return render(request, 'assignments/student_activity.html', {'activities': activities})
