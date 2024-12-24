from django import forms
from .models import Users, Collector1
from django.contrib.auth import authenticate

# User Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = Users.objects.get(username=username)
            if user.password != password:
                raise forms.ValidationError("Invalid login credentials")
        except Users.DoesNotExist:
            raise forms.ValidationError("Invalid login credentials")
        return cleaned_data


# Collector Login Form
class CollectorLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            collector = Collector1.objects.get(email=email)
            if collector.password != password:
                raise forms.ValidationError("Invalid login credentials")
        except Collector1.DoesNotExist:
            raise forms.ValidationError("Invalid login credentials")
        return cleaned_data


# Admin Login Form (using Django's built-in User model)
class AdminLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(username=email, password=password)
        if not user or not user.is_staff:
            raise forms.ValidationError("Invalid admin login credentials")
        return cleaned_data
