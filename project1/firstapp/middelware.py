
def func_middelware(get_response):
    def middelware(request):
        print("function based middleware -pre request")
        response=get_response(request)
        print("function based middleware -post response")
        return response
    return middelware

class class_middeleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("class based middleware -pre request")
        response=self.get_response(request)
        print("class based middleware -post response")
        return response

    def prepare_exception(self,request,exception):
        return None 
    