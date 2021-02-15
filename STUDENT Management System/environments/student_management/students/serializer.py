#import restframe work and models
from rest_framework import serializers
from .models import Student

#for data validation blog
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ('pk', 'name', 'email', 'gender', 'semester', 'phone', 'registrationDate')


