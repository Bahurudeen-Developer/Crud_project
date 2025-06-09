from django.shortcuts import render
from django.http import HttpResponse 
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import employee


# Create your views here.

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form = EmployeeForm()

    return render(request, 'create.html',{'form':form})

def employee_list(request):
    Employee = employee.objects.all()
    return render (request, 'list.html',{'Employees':Employee})


def update_employee(request,pk):
    Employee = employee.objects.get(id=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=Employee)

        if  form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = EmployeeForm(instance=Employee)
    return render(request,'update.html',{'form':form})



def delete_employee(request , pk):
    Employee = employee.objects.get(id= pk)

    if request.method == 'POST':
        Employee.delete()

    return redirect('list')

