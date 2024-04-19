from django.urls import path

from .import views
urlpatterns =[
    path('<int:pk>/',views.edit_team,name='edit_team')
]