# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Lecture


class LectureAddForm(forms.ModelForm):
    chapter_id = forms.ChoiceField(choices= (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),))
    file_type= forms.ChoiceField(choices= (('pdf', 'pdf'),('ppt', 'ppt'),('image', 'image'),('doc', 'doc'),('video', 'video'),))
    topic_id = forms.ChoiceField(choices= (('.1', '.1'),('.2', '.2'),))

    class Meta:
        model = Lecture
        fields = ['topic_id', 'topic_name', 'file_type','file','image','reference','chapter']
        exclude = ()
        widgets = {
            'image': forms.FileInput(),
            'file': forms.FileInput(),
        }