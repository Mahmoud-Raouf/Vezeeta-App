from rest_framework import serializers
from accounts.models import Profile , Comment , Appointment

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('who_i','name','surname','subtitle','address','address_detail',
                    'price','join_us','number_phone','working_hours',
                    'image','type_doctors','Waiting_time','facebook',
                    'twitter','google','doctor','Specialist_doctor')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comments' )

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('name', 'number', 'email' )