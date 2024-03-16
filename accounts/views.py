from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserRegisterSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.http import HttpResponse
from rest_framework.parsers import JSONParser,FileUploadParser
from rest_framework.decorators import api_view
import io
from rest_framework.renderers import TemplateHTMLRenderer
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
class Register_Create(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/register.html'
    def get(self, request):
            user = CustomUser.objects.all
            serializer = UserRegisterSerializer(user,many=True)
            return Response({'serializer': serializer, 'user': user})
        
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serialized = UserRegisterSerializer(data=request.data)
        print(request.data['select'])
        CustomUser.objects.create_user(
              self.request.data['email'],
              name=self.request.data['name'],
              phone=self.request.data['phone'],
              group=self.request.data['select'],
              session=self.request.data['select2'],
              password=self.request.data['password']

            )
        if serialized.is_valid():
            CustomUser.objects.create_user(
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("data invalid")

def home(request):
    if request.user.is_authenticated:
        return render(request,'home/home.html')
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
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'registration/verify_email_confirm.html')

        
def verify_email_complete(request):
    return render(request, 'registration/verify_email_complete.html')