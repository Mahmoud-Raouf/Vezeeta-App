from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('doctors/' , views.doctors_list , name='doctors_list'),
    path('signup/' , views.signup , name='signup'),
    path('login/' , views.user_login , name='login'),
    path('myprofile/' , views.profile , name='profile'),
    path('update/' , views.update_profile , name='update_profile'),
    path('requests/<slug:slug>/' , views.requests , name='requests'),
    path('<slug:slug>/', views.doctors_detail, name='doctors_detail'),
    path('appointment/<slug:slug>/' , views.appointment , name='appointment'),
    path('requests_delete/<int:id>/' , views.requests_delete , name='requests_delete'),



]