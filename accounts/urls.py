from django.contrib import admin
from django.urls import path,include, re_path
from accounts import views
import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    #path('', views.frontpage_view.as_view()),
    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    #path('json-data', views.carousel, name='carousel'),
    path('register/', views.Register_Create.as_view(),name='register'),
    path('login/', views.Register_Create.as_view(),name='login'),
    path('home/', views.home,name='home'),
    path('password_change/', views.password_change,name='password_change'),
    path('verify-email/', views.verify_email, name='verify-email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),

    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),


]
