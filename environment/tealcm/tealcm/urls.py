from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from userprofile.views import signup,myaccount

urlpatterns = [

    path('chat/',include('chat.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/',include('dashboard.urls')),
    path('dashboard/clients/',include('client.urls')), 
    path('dashboard/myaccount/',myaccount,name='myaccount'),
    path('dashboard/team/', include('team.urls')),
    path('lead/',include('lead.urls')),
    path('',include('crm.urls')),
    path('sign-up/',signup,name='signup'),
    path('log-in/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('log-out/',views.LogoutView.as_view(),name='logout')


]
  