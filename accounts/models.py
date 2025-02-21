from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .manager import UserManager

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

class CustomUser(AbstractUser):
    username=None
    first_name=None
    last_name=None
    email=models.EmailField(max_length=100, unique=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20, unique=True)
    roll=models.CharField(max_length=100, null=True)
    session=models.CharField(max_length=100, null=True)
    group=models.CharField(max_length=100,  null=True)
    college=models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    email_is_verified=models.BooleanField(default=False,null=True)

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','phone']
    objects=UserManager()
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('registration/user_reset_password.html', context)
    email_plaintext_message = render_to_string('registration/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
    