from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_list_or_404
from .forms import AddLeadForm
from.models import Lead
from client.models import client 
from team.models import Team
@login_required
def leads_list(request):
    leads=Lead.objects.filter(created_by=request.user,converted_to_client=False)

    return render(request,'leads_list.html',{'leads': leads})

# adding page of details to the leads

@login_required
def leads_detail(request,pk):
    lead= get_list_or_404(Lead,created_by=request.user,pk=pk)
    lead=Lead.objects.filter(created_by=request.user).get(pk=pk)


    return render(request,'leads_detail.html',{'lead':lead})

#delete user from lead list
@login_required
def leads_delete(request,pk):
    lead= get_list_or_404(Lead,created_by=request.user,pk=pk)
    lead=Lead.objects.filter(created_by=request.user).get(pk=pk)
    lead.delete()
    messages.success(request,'The Lead was deleted')
    return redirect('leads_list')

@login_required
def add_lead(request):
    global team
    team=Team.objects.filter(created_by=request.user)[0]
    if request.method=='POST':  
    
        form =AddLeadForm(request.POST)

        if form.is_valid():
    
           lead=form.save(commit=False)
           lead.created_by =request.user
           lead.team=team
           lead.save()
           messages.success(request,'The Lead was added successful')
           return redirect('dashboard')
    else:
       form=AddLeadForm()
    return render(request,'add_lead.html',{'form':form,'team':team})

@login_required
def convert_to_client(request,pk):
    global client
    lead=get_list_or_404(Lead,created_by=request.user,pk=pk)
    lead=Lead.objects.filter(created_by=request.user).get(pk=pk)
    team=Team.objects.filter(created_by=request.user)[0]

    client = client.objects.create(
     name=lead.name,
     email=lead.email,
     description =lead.description,
    created_by=request.user,
    team =team,
    )

    lead.converted_to_client= True
    lead.save()
    messages.success(request,'The Lead was converted to client')

    return redirect('leads_list')
