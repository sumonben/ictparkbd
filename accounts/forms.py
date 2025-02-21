# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "phone")

class UserEditForm(forms.ModelForm):
    college = forms.ChoiceField(choices= (('Ajijul Hoque College', 'Ajijul Hoque College'),('Govt. Mujibur Rahman Women College', 'Govt. Mujibur Rahman Women College'),),widget=forms.Select(attrs={'style': 'width:350px;height:30px;text-align:center;border-radius: 20px;box-shadow: inset -8px -8px 8px #cbced1, inset 8px 8px 8px #fff;'}))
    session = forms.ChoiceField(choices= (('2023-24', '2023-24'),('2024-25', '2024-25'),('2025-26', '2025-26'),('2026-27', '2026-27'),('2027-28', '2027-28'),),widget=forms.Select(attrs={'style': 'width:350px;height:30px;text-align:center;border-radius: 20px;box-shadow: inset -8px -8px 8px #cbced1, inset 8px 8px 8px #fff;'}))
    group = forms.ChoiceField(choices= (('Science', 'Science'),('Humanities', 'Humanities'),('Bussiness Studies', 'Business Studies'),),widget=forms.Select(attrs={'style': 'width:350px;height:30px;text-align:center;border-radius: 20px;box-shadow: inset -8px -8px 8px #cbced1, inset 8px 8px 8px #fff;'}))

    class Meta:
        model = CustomUser
        fields = [ 'email', 'name', 'phone', 'roll', 'session','group','college','image','email_is_verified']
        exclude = ()
        widgets = {
            'image': forms.FileInput(),
            'roll': forms.TextInput(),
        }