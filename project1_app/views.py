from django.shortcuts import render
from .models import task_list

def  home_post(request):
    all_task = task_list.objects.all()
    completed_tasks = all_task.filter(completed=True).count()
    task_count = all_task.count()
    if(task_count >0):
        progress = (completed_tasks / all_task.count()) * 100
    else:
        progress = 100
    return render(request, 'stats.html', {'progress': progress, 'completed': completed_tasks, 'pending': task_count - completed_tasks})


    
    
        