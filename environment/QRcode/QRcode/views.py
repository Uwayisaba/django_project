from django.shortcuts import render
from bookstore.models import BookStore
def home_view(request):
    name ="Welcome to "

    obj =BookStore.objects.get(id=1)


    context ={
        'name': name,
        'obj':obj,
   }
    
    return render(request,'home.html',context)