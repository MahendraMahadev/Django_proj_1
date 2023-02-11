from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(Request):
   # return HttpResponse("<h1 style= background:orange>Hello!!! this is my first Django App</h1>")
   my_dict = {'insert_me': "I am coming from subfolder app1_home/Reg.html"}
   return render(Request, 'app1_home/Reg.html', context=my_dict)



