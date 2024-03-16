from django.shortcuts import redirect, render
from frontpage.models import Carosel
from django.views.decorators.csrf import csrf_exempt
from .serializers import frontpageSerializer
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

class Carousel_Create(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontpage/add-carousel.html'
    def get(self, request):
        if self.request.user.is_staff:
            carousel = Carosel.objects.all
            serializer = frontpageSerializer(carousel,many=True)
            return Response({'serializer': serializer, 'carousel': carousel})
        return HttpResponse('You have no permission to add carousel')
    def post(self, request):
        
        serializer = frontpageSerializer( data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('create_carousel')


class Carousel_Up_Del_Retr(RetrieveUpdateDestroyAPIView):
    queryset=Carosel.objects.all()
    serializer_class=frontpageSerializer



class frontpage_view(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontpage/frontpage.html'
    def get(self, request):
        carousel = Carosel.objects.all
        serializer = frontpageSerializer(carousel,many=True)
        return Response({'serializer': serializer, 'carousel': carousel})
# Create your views here.
def frontpage(request):
    carosel=Carosel.objects.all()
    return render(request,'frontpage/frontpage.html',{'carosel':carosel})

'''@csrf_exempt
def add_carousel(request):
    if request.method=="POST":
        if request.POST.get('title')==None:
            data=request.body
            print(data)
            json_data=io.BytesIO(data)
            python_data=JSONParser().parse(json_data)
            print(python_data)
            serializeData=frontpageSerializer(data=python_data)
            if serializeData.is_valid():
                print(python_data)
                serializeData.save()
                response={'msg':'Data Inserted Succesfully!'}
                json_data=JSONRenderer().render(response)
                return HttpResponse(json_data, content_type='application/json')
            jsondata=JSONRenderer().render({'msg':'you are wrong!'})
            return HttpResponse(jsondata, content_type='application/json')
        else:
            serializer = frontpageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data)
            return HttpResponse(serializer.errors, status=400)
            carousel=Carosel()
            carousel.cid=request.POST.get('title')
            carousel.cname=request.POST.get('name')
            carousel.ctext=request.POST.get('body')
            if len(request.FILES)!=0:
                carousel.cimage=request.FILES['image']
            
            carousel.save()
        return redirect('/')

    return render(request,'frontpage/add-carousel.html',{'carousel':"carousel"})

@csrf_exempt
def add_carousel(request):
    if request.method=="POST":
        data={
            'cid':request.POST.get('title'),
            'cname':request.POST.get('name'),
            'ctext':request.POST.get('body')
        }
        if len(request.FILES)!=0:
            carousel.cimage=request.FILES['image']
        
        carousel.save()
        return redirect('/')

    return render(request,'frontpage/add-carousel.html',{'carousel':"carousel"})'''


def carousel(request):
    caro=Carosel.objects.all()
    serilizer=frontpageSerializer(caro,many=True)
    json_data=JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data, content_type='application/json')