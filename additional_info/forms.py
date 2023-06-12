from django import forms

class AdditionalInfoForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    city = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    project_name = forms.CharField(max_length=255)
    latitude = forms.DecimalField(max_digits=18, decimal_places=16)
    longitude = forms.DecimalField(max_digits=18, decimal_places=16)
