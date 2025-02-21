from django.shortcuts import render
from imaplib import _Authenticator
from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Lecture,Chapter,Subject
from django.views.decorators.csrf import csrf_exempt
from .serializers import LectureSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView,RetrieveAPIView
from django.views.generic import (
    DetailView,
)
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
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
from .forms import LectureAddForm
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from payments.models import Payment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class Lecture_Create(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studymaterials/addlecture.html'
    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = LectureSerializer
    def get(self, request):
            lecture = Lecture.objects.all
            serializer = LectureSerializer(lecture,many=True)
            return Response({'serializer': serializer, 'lecture': lecture})
        
    def post(self, request):
        serialized = LectureSerializer(data=request.data)
        
        ''' Lecture.objects.create_user(
              self.request.data['email'],
              name=self.request.data['name'],
              phone=self.request.data['phone'],
              group=self.request.data['group'],
              session=self.request.data['session'],
              password=self.request.data['password']

            )'''
        if serialized.is_valid():
            serialized.save(author=request.user)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("data invalid")
    '''def get(self, request, id):
        lecture = Lecture.objects.filter(chapter_id=id).order_by('topic_id')
        return Response({'user':request.user, 'lecture': lecture})'''


class ChapterView(DetailView):
    model = Chapter
    template_name = "studymaterials/chapterview.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        lectures=Lecture.objects.filter(chapter__chapter_id__contains=pk).distinct()
        print(lectures)

       
        
            # next -> get posts with id greater than the current post id, then get the first instance 'next post'
     # previous -> get posts with id less than the current post id, then get the first instance 'previous post'
        context = {
          'lectures':lectures,
          
          
         }
        return context



   
class Lecture_Rest_Api(CreateAPIView):
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'studymaterials/addlecture.html'

    permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class = LectureSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)