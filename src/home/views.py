from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class Welcome(View):
    def get(self,request):
        return HttpResponse("<a href = '/hello'>یه نگاه به سایتم بنداز</a>")
    
class Hello(View):
    def get(self,request):
        return render(request,"home/index.html")