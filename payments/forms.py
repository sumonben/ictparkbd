# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Payment


class PaymentCreateForm(forms.ModelForm):
    email = forms.EmailField()
    month = forms.ChoiceField(choices= (('January', 'January'),('February', 'February'),('March', 'March'),('April', 'April'),('May', 'May'),('June', 'June'),))
    start_date = forms.DateInput()
    end_date = forms.DateInput()
    deadline = forms.DateInput()
    class Meta:
        model = Payment
        fields = [ 'email','user_id','phone','month','amount','start_date','end_date','status','deadline']
        exclude = ()
        widgets = {
            'start_date': forms.DateInput(
        format=('%m-%d-%y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            'end_date': forms.DateInput(
        format=('%m-%d-%y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
             'deadline': forms.DateInput(
        format=('%m-%d-%y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
        }