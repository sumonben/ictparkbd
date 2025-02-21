from django.contrib import admin
from django.urls import path,include, re_path
from studymaterials import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    #path('', views.frontpage_view.as_view(), name='home'),
    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    path('add_lecture',views.Lecture_Create.as_view() , name='add_lecture'),
    path('chapter/<int:pk>/',views.ChapterView.as_view() , name="chapter"),

    #path('create_carousel/', views.Carousel_Create.as_view(), name='create_carousel'),
    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),


]