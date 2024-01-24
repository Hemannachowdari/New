from django.shortcuts import render
from django.http import HttpResponse
import datetime

def s1(request):
    return HttpResponse("<h1>Hemannachowdari")

def s2(request):
    return HttpResponse("Palabandla")

def data_time(request):
    time = datetime.datetime.now()
    t = '<h2>Current datetime is:'+str(time)+'</h2>'
    return HttpResponse(t)

def home(request):
    return render(request, 'home.html',context={'name':"Hemannachowdari"})

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    result = a+b
    return render(request,('result.html',{'result':result }))

def emp_details(request):
    ename ="Hemannachowdari"
    eid = 34
    esal =343534
    eadd ="Basampalli"
    designation ="Software Engineer"

    context_details ={"ename":ename,"eid":eid,"esal":esal,"eadd":eadd,"designation":designation}
    return render(request, 'emp.html',context_details)

def my_details(request):
    name ="Hemannachowdari"
    sur_name ="Palabandla"
    add ="Basampalli"
    designation ="Software Engineer"

# def something(request):
#     pass
def add(a,b):
    pass