from django.contrib import admin
from django.urls import path,include, re_path
from accounts import views
import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    #path('', views.frontpage_view.as_view()),
    #path('add-carousel/', views.add_carousel, name='add-carousel'),
    #path('json-data', views.carousel, name='carousel'),
    path('register/', views.Register_Create.as_view(),name='register'),
    path('login/', views.loginView,name='login'),
    path('logout/', views.logoutView,name='logout'),
    path('profile/', views.profileView,name='profile'),
    path('updateuser/', views.updateuser,name='updateuser'),
    path('imageupdate', views.imageUpdate, name='imageupdate'),

    path('dashboard/', views.dashboard,name='dashboard'),
    path('password_change/', views.password_change,name='password_change'),    
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('verify-email/', views.verify_email, name='verify-email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),
    
    #membership URL
    


    

    #path('retr_carousel/<int:pk>', views.Carousel_Up_Del_Retr.as_view()),
    #REest_API_URL
    path('signup_api/', views.Register_Rest_Api.as_view(), name="signup_api"),
    path('password_change_api/', views.ChangePasswordView.as_view(),name='password_change_api'),
    path('login_api/', views.LoginAPIView.as_view(),name='login_api'),
    path("password_reset_api/", include('django_rest_passwordreset.urls', namespace='password_reset_api')),
    path('verify_email_api/', views.VerifyEmail.as_view(),name='verify_email_api'),
    path('user_update_api/', views.UserUpdateAPI.as_view(),name='user_update_api'),
    
    
]
