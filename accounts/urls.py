from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import update_profile


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = [
    path('update-profile/', update_profile, name='update_profile'),  # URL جدید برای به‌روزرسانی پروفایل
]
