from django.shortcuts import render, redirect
from .forms import AdditionalInfoForm
from .models import User
from django.core.exceptions import ValidationError

def additional_info_view(request):
    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            city = form.cleaned_data['city']
            location = form.cleaned_data['location']
            project_name = form.cleaned_data['project_name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            user = User(username=username, password=password, city=city, location=location, project_name=project_name,
                        latitude=latitude, longitude=longitude)
            
            try:
                user.full_clean()  # Perform full validation including latitude and longitude fields
                user.save()
                return redirect('dashboard_view')
            except ValidationError:
                pass  # Ignore validation error and continue
            

            return redirect('dashboard_view')

    else:
        form = AdditionalInfoForm()

    return render(request, 'additional_info.html', {'form': form})


def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('dashboard_view')