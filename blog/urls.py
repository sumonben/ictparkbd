from django.contrib import admin
from django.urls import path,include, re_path
from blog import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.blog_index, name='blog'),
    path('singlepost/<int:pk>/',views.PostView.as_view() , name="singlepost"),
    path('createpost/',views.creatPost , name="createpost"),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blog_posts"),
    path('showmultiple/<str:type>/<int:id>', views.showMultiple, name="showmultiple"),
    
    path('<int:year>/<int:month>/',
         views.ArticleMonthArchiveView.as_view(month_format='%m'),
         name="post_archive_month"),
    
    

    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    ##path('json-data', views.carousel, name='carousel'),
    #path('create_carousel/', views.Carousel_Create.as_view(), name='create_carousel'),
    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),


]
