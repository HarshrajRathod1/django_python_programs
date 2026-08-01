from django.http import HttpResponse
class IPBlockmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.META.get('REMOTE_ADDR')=='127.0.0.2':
            response=HttpResponse('<h1>This ip address is blocked</h1>')
            return response
        response=self.get_response(request)
        print("middleware-post")
        return response

class ContentTypemiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if 'text/html' in request.headers.get('Accept'):
            return self.get_response(request)
        return HttpResponse('<h1>Text not in text/html extenstion</h1>')

class TitleChangeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response= self.get_response(request)
        response.write('<title>Harshraj</title>')
        return response



        
    