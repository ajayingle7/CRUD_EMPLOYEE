from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.



def signupView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/signup.html'
    context = {'form':form}

    if request.method=='POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()



    return render(request,template_name,context)


def loginView(request):
    template_name ='AUTH_APP/login.html'
    context = {}

    if request.method=='POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        user = authenticate(username=un, password=pw)

        if user is not None:
            login(request,user)

            return redirect('empview')



    return render(request,template_name,context)


def logoutView(request):
    logout(request)

    return redirect('loginview')

