from django.http import HttpResponse
from django.shortcuts import redirect, render
from project1_app.models import task_list

def home_view(request):
    if request.method == 'POST':
        print(request.POST)
        task_name = request.POST.get('task_name')
        task_list.objects.create(task=task_name)
        return redirect('/')
    all_tasks = task_list.objects.all().order_by('completed')
    return render(request, 'home.html', {'initial_tasks': all_tasks})    

def checked_task(request, task_id):
    task = task_list.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')  

def delete_task(request, task_id):
    task = task_list.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def about_view(request):
    #return HttpResponse("This is the About Line.")
    return render(request, 'about.html')