from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm  # فرض بر این  که فرم‌ها رو درست کردی

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # هدایت به صفحه پروفایل پس از موفقیت
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'form': form})
