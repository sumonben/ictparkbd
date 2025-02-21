# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post,CommentGuest, Comment,Category,Tag
from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'style': 'font-size:25px;width:85%;height:40px;border-radius: 10px;box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;'}),label='শিরোনাম')
    subtitle=forms.CharField(widget=forms.TextInput(attrs={'style': 'font-size:25px;width:80%;height:40px;border-radius: 10px;box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;'}),label='উপ-শিরোনাম')

    meta_description = forms.ChoiceField(choices= (('Science', 'কবিতা'),('Humanities', 'গল্প'),('Bussiness Studies', 'বিজ্ঞান'),),label='মেটা',widget=forms.Select(attrs={'style': 'width:40%;height:30px;text-align:center;border-radius: 20px;box-shadow: inset -8px -8px 8px #cbced1, inset 8px 8px 8px #fff;'}))
    body=forms.CharField(widget=CKEditorWidget(attrs={'style': 'font-size:25px;width:80%;border-radius: 10px;box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;'}),label='মূল অংশ')
    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'style': 'font-size:25px;border-radius: 10px;box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;'}),
        label='ক্যাটাগরি'
        
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'style': 'font-size:25px;border-radius: 10px;box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;'}),
        label='ট্যাগ'
        
    )
    image=forms.ImageField(label='ছবি যুক্ত করুন')
    class Meta:
        model = Post
        fields =[ 'title', 'subtitle', 'body', 'meta_description', 'categories','tags', 'image']
        
    widgets={
            'title': forms.TextInput(attrs={'style': 'width:500px'}),
            'meta_description': forms.Select(attrs={'style': 'width:200px'}),
             'image': forms.FileInput(),

            }
class CommentGuestForm(forms.ModelForm):
    class Meta:
        model = CommentGuest
        fields = ('name', 'email', 'content') 

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'), label='মন্তব্য')
    
    class Meta:
        model = Comment
        fields = ('content',) 