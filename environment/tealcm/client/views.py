from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404,redirect, render,get_object_or_404

#@login_required
#def clients_add(request):

@login_required 
def clients_list(request):
     clients= client.objects.filter(created_by=request.user)
     return render (request,'clients_list.html',{'clients':clients})

@login_required
def clients_detail(request,pk):
    global client
    client =get_list_or_404(client,created_by=request.user,pk=pk)

    return render (request,'clients_detail.html',{'client':client})
