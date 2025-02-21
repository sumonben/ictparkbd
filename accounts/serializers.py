from imaplib import _Authenticator
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from .models import CustomUser
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

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email', 'name', 'phone', 'session','group','password']
        
        
        def save(self):
            password=self.validated_data['password']
            password2=self.validated_data['password2']
            if password!=password2:
                raise serializers.ValidationError({'error':'Password does not match'})
            if CustomUser.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error':'Email already exists'})
            account =CustomUser(email=self.validated_data['email'],name=self.validated_data['name'], phone=self.validated_data['phone'],session=self.validated_data['session'],group=self.validated_data['group'])
            account.set_password(password)
            account.save(using=self.db)
            return account

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    name = serializers.CharField(
        required=True,
        
        )
    
    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    
    session = serializers.CharField(
        required=True,
        
        )
    
    group = serializers.CharField(
        required=True,
        
        )
    password = serializers.CharField(write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = CustomUser
        fields = (
                        'email', 'name', 'phone', 'session','group','password'

        )
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user=super(UserSerializer, self).create(validated_data)
        
        return user
    
        
    
          
class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if CustomUser.objects.filter(email=email).exists():
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)

            else:
                msg = {'detail': 'Phone number is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
class ChangePasswordSerializer(serializers.Serializer):
        model = CustomUser

        """
        Serializer for password change endpoint.
        """
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)



class VerifyEmailSerializer(serializers.Serializer):
    
        model = CustomUser

        """
        Serializer for password change endpoint.
        """
        email = serializers.CharField(required=True)
        

class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=CustomUser
         fields=('email','password') 
         


class UserUpdateSerializer(serializers.ModelSerializer):
    

    
    name = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': ' Name'}
        )
    phone = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': ' Phone'}
        )
    session = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': ' Session'}
        )
    group = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': ' Group'}
        )
    roll = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': ' Roll'}
        )
    college = serializers.CharField(
        required=False,
        
        help_text='Leave empty if no change needed',
        style={'input_type': 'text', 'placeholder': 'College Name', 'hight':'30px'}
        )
    image = serializers.ImageField(
        required=False,
        
        )

    class Meta:
        model = CustomUser
        fields = (
                        'name','phone','session','group','roll','college','image'

        )    