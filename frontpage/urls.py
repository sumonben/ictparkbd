from django.contrib import admin
from django.urls import path,include, re_path
from frontpage import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.frontpage_view.as_view(), name='home'),
    path('about/<str:pk>', views.about, name='about'),
    path('accountabout/<str:pk>', views.about, name='accountabout'),
    path('membership/<str:pk>', views.memberShip,name='membership'),
    path('accountmembership/<str:pk>', views.memberShip,name='accountmembership'),

    path('media/<str:pk>', views.mediaCenter, name='media'),
    path('accountmedia/<str:pk>', views.mediaCenter, name='accountmedia'),


    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    path('json-data', views.carousel, name='carousel'),
    path('create_carousel/', views.Carousel_Create.as_view(), name='create_carousel'),
    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),
    

]
