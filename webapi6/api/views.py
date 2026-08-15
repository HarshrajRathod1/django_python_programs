from django.shortcuts import render
from api.models import  Student
from api.serializer import StudentSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.

class Student_view(APIView):
    def get(self,request):
        qs=Student.objects.all()
        studser=StudentSerializer(qs,many=True)
        studs=studser.data
        return Response(studs)
    def post(self,request):
        studser=StudentSerializer(request.data)
        stud=studser.data
        Student.objects.create(**stud)
        return Response({'msg':'student created!'})

class Student_oprations(APIView):
    def get(self,request,pk):
        stud=Student.objects.get(rno=pk)
        studser=StudentSerializer(stud)
        studdata=studser.data
        return Response(studdata)

    def put(self,request,pk):
        stud=Student.objects.get(rno=pk)
        data=StudentSerializer(request.data).data
        stud.name=data['name']
        stud.course=data['course']
        stud.save()
        return Response({'msg':'Student Updated!'})

    def delete(self,request,pk):
        Student.objects.filter(rno=pk).delete()
        return Response({'msg':'Student Deleted!'})




'''
Function Based View 

@api_view(['GET'])
def getall(request):
    qs=Student.objects.all()
    qsser=StudentSerializer(qs,many=True)
    stud_data=qsser.data
    return Response(stud_data)

@api_view(http_method_names=['GET'])
def getstud(request,rno):
    stud=Student.objects.get(rno=rno)
    studser=StudentSerializer(stud)
    studdata=studser.data
    return Response(studdata)


@api_view(['POST'])
def create_stud(request):
    studser=StudentSerializer(request.data)
    studdata=studser.data
    Student.objects.create(**studdata)
    return Response({'msg':'student Created'})

@api_view(['DELETE'])
def delete_stud(request,rno):
    stud=Student.objects.get(rno=rno)
    stud.delete()
    return Response({'msg':'Student Deleted!'})

@api_view(http_method_names=['PUT'])
def update_stud(request,rno,course):
    Student.objects.filter(rno=rno).update(course=course)
    return Response({'msg': 'Student Updated'})

'''

