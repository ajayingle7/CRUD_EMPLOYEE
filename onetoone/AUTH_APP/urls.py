from django.urls import path
from .views import signupView,loginView,logoutView


urlpatterns = [

    path('signup/', signupView, name='signupview'),
    path('login/', loginView, name='loginview'),
    path('logout/', logoutView, name='logoutview')


]