from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('task_list')
    else:
        form=TaskForm()

    return render(request,'add.html',{'form':form})
    
def view_tasks(request):
        tasks=Task.objects.all().order_by('-id')
        context={
            'tasks':tasks
        }
        return render(request,'view_task.html',context)
    
def edit_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if request.method =='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=task)
    return render(request,'edit_task.html',{'form':form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
    
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completion_status = not task.completion_status
    task.save()
    return redirect('task_list')
    


