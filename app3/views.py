from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3_str(request):
    return HttpResponse("<h1>Hello World! This is app3 string response</h1>")

def india(request):
    return render(request,'india.html')