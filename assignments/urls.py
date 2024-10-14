from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet
from .views import student_activity

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = [
    path('my-activities/', student_activity, name='student_activity'),  # URL جدید برای فعالیت‌های دانشجو
]
