from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from EventRegistrationHEApp import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('registeredusers/', views.ER_Registered_User, name='registeredusers'),
    path('registerform/', views.registerdata, name='registerform'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('userd/<value>', views.ER_Registered_User_details, name='userd'),
    path('userdetails/', views.ER_Registered_User_details, name='userdetails')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)