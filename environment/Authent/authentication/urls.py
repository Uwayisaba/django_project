from django.urls import path
from .views import HomePage,Register,Login,Test,SendMail


urlpatterns=[
    path('home/',HomePage,name="home-page"),
    path('register/',Register,name="register-page"),
    path('login/',Login,name="login-page"),
    path('test/',Test,name="test-page"),
    path('send_mail/',SendMail,name="send-mail"),
]