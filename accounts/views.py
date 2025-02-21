from imaplib import _Authenticator
from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import CustomUser
from blog.models import Post,Comment,CommentGuest,Profile,Category,Tag

from django.views.decorators.csrf import csrf_exempt
from .serializers import LoginSerializer, LoginUserSerializer, UserRegisterSerializer,ChangePasswordSerializer,VerifyEmailSerializer,UserSerializer,UserUpdateSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView,RetrieveAPIView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import JSONParser,FileUploadParser
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
import io
from django.contrib.auth import login,authenticate,logout
from rest_framework.renderers import TemplateHTMLRenderer,BrowsableAPIRenderer
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
from .forms import UserEditForm
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from payments.models import Payment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import validate_email
from django import forms

class Register_Create(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/register.html'
    def get(self, request):
            user = CustomUser.objects.all
            serializer = UserRegisterSerializer(user,many=True)
            return Response({'serializer': serializer, 'user': user})
        

    def post(self, request):
        email_get=request.data['email']

        try:
            validate_email( request.data['email'] )
            email1= True
        except forms.ValidationError:
            email1= False
        phone1=request.data['phone']
        password1=request.data['password']
        password_confirmation1=request.data['password_confirmation']

        if email1 is False:
            email='Please enter valid Email'
        else:
            email=None
        if len(phone1) is not 11 and phone1.isdigit() is True:
            phone='Please enter valid Phone Number'
        else:
            phone=None
            
        if password1!=password_confirmation1:
            password='Password not matched'
        else:
            password=None
        
        if CustomUser.objects.filter(email=email_get).exists():
            email='Email Already Exist'
        if CustomUser.objects.filter(phone=phone1).exists():
            phone='Phone Number Already Exist'

        if email is None and password is None and phone is None:
            
          
            user=CustomUser.objects.create_user(
              self.request.data['email'],
              name=self.request.data['name'],
              phone=self.request.data['phone'],
              group=self.request.data['group'],
              session=self.request.data['session'],
              password=self.request.data['password'],
              roll=self.request.data['roll'],
              college=self.request.data['college']



            )
            
            current_site = get_current_site(request)
            email = user.email
            subject = "Verify Email"
            message = render_to_string('registration/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return render(request, "accounts/register.html", {"user":user,"success": "Account Created Succesfully, A verifcation Email sent to your email address(Find in spam if not found in inbox).verify email to activate your account "})
        else:
            print("sumon wrong")
            return render(request, "accounts/register.html", {'email': email,'phone':phone,'password':password})

        '''serialized = UserRegisterSerializer(data=request.data)
        user=CustomUser.objects.create_user(
              self.request.data['email'],
              name=self.request.data['name'],
              phone=self.request.data['phone'],
              group=self.request.data['group'],
              session=self.request.data['session'],
              password=self.request.data['password']

            )
        if user:
            return HttpResponse("Registration Successful, Your account will be active shortly")

        else:

            return HttpResponse("data invalid")'''

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    html_email_template_name='accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('dashboard')


def loginView(request):
        
    if request.method == 'GET':
        context = ''
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'accounts/login.html', {'context': context})
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        if CustomUser.objects.filter(email=email).exists() is False:
            email='Email not exist in user system. Please enter valid Email! '
            return render(request, 'accounts/login.html', {'email': email})
        user = CustomUser.objects.get(email=email)
        if user.is_active is False:
            email='Email not verified!! Please verify email to activate account '
            return render(request, 'accounts/login.html', {'email': email})
        user = authenticate(request, username=email, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            # Redirect to a success page.
            ...
        else:
            password='Your Creadentials do not match, Please try again!!'
            return render(request, 'accounts/login.html', {'password': password})
            # Return an 'invalid login' error message
 
            
def logoutView(request):
     logout(request=request)
     # message user or whatever
     return redirect('login')
 
 
def profileView(request):
    if request.user.is_authenticated:
        queryset=Payment.objects.filter(user_id=request.user.pk)
        post=Post.objects.filter(author=Profile.objects.filter(user=request.user).first()).select_related('author').order_by('-date_created')
        page = request.GET.get('page', 1)
        paginator = Paginator(post, 5)
        try:
         post = paginator.page(page)
        except PageNotAnInteger:
         post = paginator.page(1)
        except EmptyPage:
         post = paginator.page(paginator.num_pages)
        return render(request,'dashboard/profile.html',{'queryset':queryset,'post':post})
    else:
        return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        users=CustomUser.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(users, 8)
        try:
         users = paginator.page(page)
        except PageNotAnInteger:
         users = paginator.page(1)
        except EmptyPage:
         users = paginator.page(paginator.num_pages)
        leftmenulist={'Profile':'profile','Update Profile':'updateuser','Blog Page':'blog','News':'login','Payments':'create_payment'}
        context={'users':users,'leftmenulist':leftmenulist,'header_name':'Dashboard','page_banner':'Accounts\Dashboard','app_name':'Accounts'}

        return render(request,'dashboard/dashboard.html',context)
    else:
        return redirect('login')   

def password_change(request):
    if request.user.is_authenticated:
        return render(request,'accounts/password_change.html')
    else:
        return redirect('login')
    
    
def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('registration/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('register')
    return render(request, 'registration/verify_email.html')


def verify_email_done(request):
    return render(request, 'registration/verify_email_done.html')

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.email_is_verified = True
        user.is_active = True
        user.save()
        profile=Profile.objects.create(user=user,website='ictparkbd.com',bio=user.name)
        messages.success(request, 'Congratulations!! Your email has been verified. You can login now!!')
        return redirect('verify-email-complete')   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'registration/verify_email_confirm.html')

        
def verify_email_complete(request):
    return render(request, 'registration/verify_email_complete.html')


def updateuser(request): 
 if request.user.is_authenticated:
    user = request.user
    form = UserEditForm(instance=user)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Not success")
    return render(request, 'accounts/updateuser.html', {'form': form})

def imageUpdate(request):
     if request.user.is_authenticated:
        user=request.user
        user.image.delete()
        user.image=request.FILES.get("file")
        user.save()
     return redirect('profile')
#Serializer views for Rest API

        


class CustomChangePasswordView(ListCreateAPIView):
        renderer_classes=[TemplateHTMLRenderer]
        template_name='registration/password_change_api.html'
        serializer_class = ChangePasswordSerializer
        model = CustomUser
        permission_classes = (IsAuthenticated,)
        def get(self, request):
            user = CustomUser.objects.all
            serializer = UserRegisterSerializer(user,many=True)
            return Response({'serializer': serializer, 'user': user})
        
        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def post(self, request):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                print(response)
                return Response(response)

            print(status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          

    

 ###################################Rest_API_Classes for request Class##########################################


class Register_Rest_Api(ListCreateAPIView):
    # get method handler
    parser_classes = [JSONParser]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    
class LoginAPIView(APIView):
   def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return HttpResponse("succesfull")



class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = CustomUser
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                print(response)
                return Response(response)

            print(status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmail(UpdateAPIView):
        serializer_class = VerifyEmailSerializer
        model = CustomUser
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if request.user.email_is_verified != True:
                    current_site = get_current_site(request)
                    
                    email = request.user.email
                    subject = "Verify Email"
                    message = render_to_string('registration/verify_email_message.html', {
                        'request': request,
                        'user': request.user,
                        'domain': current_site.domain,
                        'uid':urlsafe_base64_encode(force_bytes(request.user.pk)),
                        'token':default_token_generator.make_token(request.user),
                    })
                    email = EmailMessage(
                        subject, message, to=[email]
                    )
                    email.content_subtype = 'html'
                    email.send()
                print(status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateAPI(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def update(self, request, *args, **kwargs):
        user_data = request.data
        user_serializer = self.serializer_class(request.user, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        response = {'user': user_serializer.data}
        return Response(response)

   
