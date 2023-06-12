from django.shortcuts import render, redirect
from additional_info.models import User

def dashboard_view(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})




# Google API Key AIzaSyCWAkaYNeGI0g0lNoOzF0P0ZG1RLo45Tss