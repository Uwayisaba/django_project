from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns=[
    path('',views.leads_list,name='leads_list'),
    path('add-lead/',views.add_lead,name='add_lead'),
    path('<int:pk>/delete/',views.leads_delete,name='leads_delete'),
    path('<int:pk>/',views.leads_detail,name='leads_detail'),
    path('<int:pk>/convert',views.convert_to_client,name='leads_convert'),
 ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
