from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_str(request):
    return HttpResponse("<h1>Hello World! This is app2 string response</h1>")

def rcb(request):
    return render(request,'rcb.html')
