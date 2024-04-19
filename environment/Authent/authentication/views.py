from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def HomePage(request):
   return render(request,'index.html',{})
def Register(request):
     if request.method=='POST':
         fname=request.POST.get('fname')
         lname=request.POST.get('lname') 
         Uname=request.POST.get('Uname')
         Email=request.POST.get('Email')
         pswd=request.POST.get('pswd')

         new_user=User.objects.create_user(Uname,Email,pswd) 
         new_user.first_name=fname
         new_user.last_name=lname

         new_user.save()
         return redirect('login-page')


     return render(request,'register.html',{})

def Login(request):
     if request.method=='POST':

        Username=request.POST.get('Uname')
        password=request.POST.get('pswd')

        user= authenticate(request,username=Username,password=password) 
         
        if user is not None:
           login(request,user)
           return redirect('home-page')
        else:
          return HttpResponse('Error ,user does not exist')

     return render(request,'login.html',{})
def Test(request):
    return render(request,'test.html',{})
   
   
def SendMail(request):
    if request.method =='POST':
        name=request.POST['name']
        sender_mail=request.POST['email']
        msg=request.POST['msg']
        #send email
        email= EmailMessage( 
            'Test Email',#subject
            f'Hi There {name}! \n ,Thank you for connecting us. This is your message: \n \n {msg}', #message
            settings.EMAIL_HOST_USER,#Sender
            [sender_mail] #receiver
        )

        email.fail_silently=True
        email.send()


    return render(request,'send_email.html',{})
    
