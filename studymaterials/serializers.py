from rest_framework import serializers
from imaplib import _Authenticator
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from .models import Lecture
from accounts.serializers import UserSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import messages

class LectureSerializer(serializers.ModelSerializer):
    chapter_id = serializers.IntegerField(
        required=True,
        )
    chapter_name = serializers.CharField(
        required=True,
        
        )
    
    topic_id = serializers.CharField(
        required=True,
        )
    
    topic_name = serializers.CharField(
        required=True,
        
        )
    author = UserSerializer(read_only=True)
    file_type = serializers.CharField(
        required=True,
        
        )
    
    file = serializers.FileField(
        required=True,
        
        )
    
    image = serializers.ImageField(
        required=False,
        
        )
    reference = serializers.CharField(
        required=False,
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': 'Reference'})

    class Meta:
        model = Lecture
        fields = (
                        'chapter_id', 'chapter_name', 'topic_id', 'topic_name','author','file_type','file','image', 'reference'

        )

   