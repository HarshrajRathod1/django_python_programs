from rest_framework import serializers

class EmployeeSerializers(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField()
    job=serializers.CharField()
    sal=serializers.FloatField()