from django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('app2_str/',app2_str,name='app2_str'),
    path('rcb/',rcb,name='rcb'),

]