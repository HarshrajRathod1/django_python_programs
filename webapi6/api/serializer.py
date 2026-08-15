from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    rno=serializers.IntegerField()
    name=serializers.CharField()
    course=serializers.CharField()