from imaplib import _Authenticator
from rest_framework import serializers
from django.contrib.auth import get_user_model 
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['email', 'name', 'phone', 'roll', 'session','group','college','image']
        
        '''def create(self, validated_data):
            user = get_user_model().objects.create(**validated_data)
            CustomUser.objects.create(user=user)
            return user'''
            
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