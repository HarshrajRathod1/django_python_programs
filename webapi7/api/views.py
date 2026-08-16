from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api.models import Employee
from api.serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

@method_decorator(decorator=csrf_exempt,name="dispatch")
class emp_view(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        empser=EmployeeSerializer(qs,many=True)
        emp=empser.data
        return Response(emp)
    def post(self,request):
        empser=EmployeeSerializer(data=request.data)
        if empser.is_valid():
            empser.save()
            return Response({'msg':'Employee Created'})
        else:
            return Response({'msg':'Employee Details Invalid'})

class employee_view(APIView):
    def get(self,request,pk):
        try:
            emp=Employee.objects.get(eno=pk)
            empser=EmployeeSerializer(emp).data
            return Response(empser,status=200)
        except:
            return Response({'msg':'Invalid Employee'},status=400)

    def put(self,request,pk):
        try:
            emp=Employee.objects.get(eno=pk)
        except:
            return Response({'msg':'Invalid Employee'},status=400)
        empser=EmployeeSerializer(emp,data=request.data)
        if empser.is_valid():
            empser.save()
            return Response({'msg':'Employee Updated'},status=200)
        else:
            return Response({'msg':'Invalid Employee'},status=400)

        

        '''
        empser=EmployeeSerializer(request.data)
        empdata=empser.data
        try:
            emp=Employee.objects.get(eno=empdata['eno'])
            empnewser=EmployeeSerializer(emp,data=empdata)
            if empnewser.is_valid():
                empnewser.save()
                return Response({'msg':'Employee Updated'},status=200)
            else:
                return Response({'msg':'Invalid Employee'},status=400)
        except:
            return Response({'msg':'Invalid Employee'},status=400)'''
    
    

    def delete(self,request,pk):
        try:
            Employee.objects.filter(eno=pk).delete()
            return Response({'msg':'Employee Deleted'},status=200)
        except:
            return Response({'msg':'Invalid Employee'},status=400)
