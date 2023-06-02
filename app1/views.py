from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_str(request):
    return HttpResponse("<h1>Hello World! This is app1 string response</h1>")

def csk(request):
    return render(request,'csk.html')
