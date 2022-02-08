from django.shortcuts import render,redirect
from .forms import  EmpForm,RoleForm
from .models import Role,Emp
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def empView(request):
    template_name = 'app1/empview.html'
    form = EmpForm()
    context = {'form':form}

    if request.method=='POST':
        form = EmpForm(request.POST)

        if form.is_valid():
            form.save()



    return render(request,template_name,context)


@login_required()
def roleView(request):
    template_name = 'app1/roleview.html'
    form = RoleForm()

    if request.method=='POST':
        form = RoleForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request,template_name,context)


@login_required()
def empdataView(request):
    template_name='app1/empdata.html'
    data = Emp.objects.all()

    context = {'data':data}

    return render(request,template_name,context)



def updateView(request,id):
    template_name = 'app1/empview.html'
    obj = Emp.objects.get(eid=id)
    form = EmpForm(instance=obj)

    if request.method=='POST':
        form = EmpForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

            return redirect('empdataview')




    context = {'form':form}

    return render(request,template_name,context)



def deleteView(request,id):

    template_name = 'app1/confirm.html'
    obj = Emp.objects.get(eid= id)

    if request.method=='POST':
        obj.delete()

        return redirect('empdataview')



    context = {'data':obj}

    return render(request,template_name,context)





