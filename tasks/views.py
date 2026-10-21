from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tasks

@login_required
def home_page(request):
    return render(request, "index.html")


@login_required
def task_mng(request):
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        new_task = Tasks.objects.create(
            title = title,
            description = description,
            priority = priority,
            due_date = due_date,
            user_id = request.user.id
        )
        new_task.save()
        messages.success(request, "Task is created successfully !")
        return redirect("tasks:manage")

    return render(request, "manage.html")