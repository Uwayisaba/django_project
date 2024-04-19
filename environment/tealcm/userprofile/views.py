from django.contrib.auth.decorators import login_required
from urllib import request
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

from .models import Userprofile
from team.models import Team


def signup(request):
        global form
        if request.method=='POST':   
          form=UserCreationForm(request.POST)
          if form.is_valid():
            user=form.save()
            Userprofile.objects.created(user=user)
            team=Team.objects.create(name='the team name',created_by_=request.user)
            team.members.add(request.user)
            team.save()
            
            return redirect('/log-in')
        else:

         form =UserCreationForm()

        return render(request,'signup.html',{'form':form})

@login_required
def myaccount(request):
    team=Team.objects.filter(created_by=request.user)[0]
    return render(request,'myaccount.html',{'team':team})