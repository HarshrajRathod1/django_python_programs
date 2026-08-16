from rest_framework import serializers
from api.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields=['rno']

    def validate_sal(self, sal):
        if sal<=0:
            raise serializers.ValidationError("Salary is greater than Zero")
        else:
            return sal
