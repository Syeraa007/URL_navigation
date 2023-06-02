from django.urls import path
from app1.views import *

app_name='app1'
urlpatterns = [
    path('app1_str/',app1_str,name='app1_str'),
    path('csk/',csk,name='csk'),
]