from django.shortcuts import render, redirect
from .models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            # User already exists, redirect to dashboard.html
            return redirect('dashboard_view')
        except User.DoesNotExist:
            # User does not exist, create a new user and redirect to additional_info.html
            user = User(username=username, password=password)
            user.save()
            return redirect('additional_info')
    return render(request, 'login.html')
