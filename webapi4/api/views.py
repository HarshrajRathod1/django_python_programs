from django.shortcuts import render
from django.views import View
import json
from api.models import Student
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class MixinClass():
    def bytes_json(self,b):
        s=b.decode('utf-8')
        stud=json.loads(s)
        return stud

    def dict_json(self,d):
        data=json.dumps(d)
        return data



class Student_view(View,MixinClass):

    def post(self,request,**kwargs):
        stud=super().bytes_json(request.body)
        try:
            Student.objects.create(**stud)
            return JsonResponse({'msg':'Student Created !'})
        except:
            return JsonResponse({'msg':'Plz enter unique Roll no'})

    def get(self,request,*vargs,**kwargs):
        try:
            stud=Student.objects.get(rollno=kwargs['rollno'])
            stud_dict={'rollno':stud.rollno,'name':stud.name,'course':stud.course,'fee':stud.fee}
            stud=super().dict_json(stud_dict)
            return JsonResponse(stud,safe=False)
        except:
            return JsonResponse({'msg':'Rollno invalid'})

    def put(self,request,*vargs,**kwargs):
        stud=super().bytes_json(request.body)
        try:
            student=Student.objects.get(rollno=stud['rollno'])
            student.fee=student.fee+stud['fee']
            student.save()
            return JsonResponse({'msg':'salary updated'},status=200)
        except:
            return JsonResponse({'msg':'Rollno Invalid'},status=400)

    def delete(self,request,*vargs,**kwargs):
        try:
            Student.objects.get(rollno=kwargs['rollno']).delete()
            return JsonResponse({'msg':'Student Deleted'},status=200)
        except:
            return JsonResponse({'msg':'Invalid Rollno'},status=400)

