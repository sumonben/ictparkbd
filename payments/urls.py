from django.contrib import admin
from django.urls import path,include, re_path
from payments import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('create_payment', views.CreatePayment, name='create_payment'),
    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    
    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),


]
