from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Team
from .forms import TeamForm

# create edit page of teams
@login_required
def edit_team(request,pk):
    team=get_object_or_404(Team, created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)

        if form.is_valid():
            form.save()
            messages.success(request,'The Changes was saved!')
            return redirect('myaccount')
    else:

        form=TeamForm(instance=team)

    return render(request,'edit_team.html',{
            'team':team, 
            'form':form})


