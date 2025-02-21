from django.shortcuts import redirect, render
from .models import Carosel,News
from accounts.models import CustomUser
from studymaterials.models import Lecture,Chapter,Subject
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        chapters = Chapter.objects.all
        news = News.objects.all
        #chapters="sumon"
        #for chapter in singlepost:
        # print(chapter.name)
        serializer = frontpageSerializer(carousel,many=True)
        return Response({'serializer': serializer, 'carousel': carousel, 'chapters': chapters, 'news': news})
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


def about(request,pk):
    
    leftmenulist={
        'Mission':"mission",
        'Vision':"vision",
        'Ideology':"ideology",}
    context={
        'url':'about',
        'leftmenulist':leftmenulist,
        'header_name':'About',
        
        'page_banner':'About/Mission',
        'app_name':'Abouts'}
    if(pk=='mission'):
        return render(request,'frontpage/about/mission.html',context)
    elif(pk=='vision'):
        return render(request,'frontpage/about/vision.html',context)
    else:
        return render(request,'frontpage/about/ideology.html',context)


 ###############Membership####################
def memberShip(request,pk):
    users=CustomUser.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(users, 2)
    try:
         users = paginator.page(page)
    except PageNotAnInteger:
         users = paginator.page(1)
    except EmptyPage:
         users = paginator.page(paginator.num_pages)    
    leftmenulist={
        'Member List':'memberlist',
        'Rule and Regulations':'rules-n-regulations',
        'code-of-conduct':'code-of-conduct',
        'Becme A Member':'register'}
    context={
        'users':users,
        'url':'membership',
        'leftmenulist':leftmenulist,
        'header_name':'Membership',
        'app_name':'Accounts'}
    if(pk=='memberlist'):
        return render(request,'accounts/membership/memberlist.html',context)
    elif(pk=='rules-n-regulations'):
        return render(request,'accounts/membership/rules_n_regulation.html',context)   
    else:
        return render(request,'accounts/register.html',context)   

        


###############Media News Image Video####################

def mediaCenter(request,pk):
    
    news=News.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 2)
    try:
         news = paginator.page(page)
    except PageNotAnInteger:
         news = paginator.page(1)
    except EmptyPage:
         news = paginator.page(paginator.num_pages)
            
    leftmenulist={
        
        'Blog Page':"blog",
        'Create Blog Post':"createpost",
        'News':"news",
        'Image Gallery':"image-gallery",
        'Viedo Gallery':'video-gallery'}
    context={
        'url':'media',
        'leftmenulist':leftmenulist,
        'header_name':'Media Center',
        'news':news,
        'page_banner':'Media/News,Image,Video',
        'app_name':'Media Center'}
    if(pk=='blog'):
        return redirect('blog')
    elif(pk=='createpost'):
        return render(request,'blog/postcreate.html',context)
    elif(pk=='image-gallery'):
        return render(request,'media/imagegallery.html',context)
    elif(pk=='video-gallery'):
        return render(request,'media/videogallery.html',context)
    else:
        return render(request,'media/news.html',context)
        
