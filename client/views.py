from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models  import Client, Task
from django.contrib.auth.models import  auth

from django.shortcuts import render

# Create your views here.
def client(request):
    return render(request, 'clientlogin.html')

def assign(request):
     if request.method == "POST":
         print('inside')
         domain = request.POST.get('domain')
         rate = request.POST.get('rate')
         task = request.POST.get('task')
         client_id= request.POST.get('cm')
         client= Client.objects.get(id=client_id)
         Task.objects.create(task_name=task, task_domain=domain , task_rate=rate,name=client)
         print('created')
         return render(request, 'clienthome.html',{'results':client})
     else:
         print('not created')
         return  render(request, 'assigntask.html')


def home(request):
    return render(request, 'clienthome.html')



def payment(request):
    return render(request, 'payment.html')

def register(request):
    if request.method =='POST':
        print('user created')
        name= request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            cl = Client(client_name=name, client_phone=phone, client_email=email
                        , client_password1=password1, client_password2=password2)
            cl.save()
            return redirect('/client/')
        else:

            return render(request, 'clientregister.html')
    else:
      return render(request, 'clientregister.html')

def login(request):
     if request.method== 'POST':
         username= request.POST['email']
         password= request.POST['password']
         user = Client.objects.filter(client_email=username, client_password1=password)


         if user is not None:
             return redirect('/client/home/')

         else:
             print('login not successfull')
             return render(request,'clientlogin.html')
     else:
         return render(request,'clientlogin.html')