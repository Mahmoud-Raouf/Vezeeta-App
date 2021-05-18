from accounts.models import Profile , Comment , Appointment
from .serializers import ProfileSerializer , CommentSerializer , AppointmentSerializer
from rest_framework import viewsets 
import django_filters.rest_framework #To import filter 




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] # To run filter with Profile API
    filter_fields = ( 'name' , 'address' , 'doctor')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] # To run filter with Profile API
    filter_fields = ( 'name' , 'email')

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] # To run filter with Profile API
    filter_fields = ( 'name' , 'number' , 'email')