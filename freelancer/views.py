from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models  import Freelancer
from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def free(request):
    return render(request, 'freelogin.html')


def home(request):
    return render(request, 'freehome.html')



def payment(request):
    return render(request, 'payment.html')


def register(request):
    if request.method =='POST':

        name= request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        domain=request.POST['domain']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            cl = Freelancer(free_name=name, free_phone=phone, free_email=email
                        , free_domain= domain,free_password1=password1, free_password2=password2)
            cl.save()
            return redirect('/freelancer/')
        else:

            return render(request, 'freeregister.html')
    else:
      return render(request, 'freeregister.html')

def login(request):
     if request.method== 'POST':
         username= request.POST['email']
         password= request.POST['password']
         user = Freelancer.objects.filter(free_email=username, free_password1=password)


         if user is not None:
             return redirect('/freelancer/home/')
             print('login successfull')
         else:
             print('login not successfull')
             return render(request,'freelogin.html')
     else:
         return render(request,'freelogin.html')

# Create your views here.
