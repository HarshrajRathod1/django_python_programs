from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.

def view1(request):
    if request.method=="GET":
        return JsonResponse({"msg":"This is a get request"})
    elif request.method=="POST":
        return JsonResponse({"msg":"This is a Post request"})
    elif request.method=="PUT":
        return JsonResponse({"msg":"This is a PUT request"})
    elif request.method=="DELETE":
        return JsonResponse({"msg":"This is a Delete Request"})

class hdfc_view(View):
    def get(request,*args,**kwarg):
        return JsonResponse({"msg":"Your current account Balance"})
    def post(request,*args,**kwargs):
        return JsonResponse({"msg":"Your have created !"})
    def put(request,*args,**kwargs):
        return JsonResponse({"msg":"Account balance is updated"})
    def delete(request,args,**kwargs):
        return JsonResponse({"msg":"Account Deleted Successfully !"})
