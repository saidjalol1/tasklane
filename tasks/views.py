from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tasks

@login_required
def home_page(request):

    if request.method == "POST" and "toggle_status" in request.POST:
        toggle_task = Tasks.objects.get(id=request.POST.get("task_id"))
        toggle_task.status = not toggle_task.status

        toggle_task.save()
        status = "done" if toggle_task.status == True else " changed"
        messages.success(request, f"{toggle_task.title} is {status}" )
        return redirect("tasks:home")


    return render(request, "index.html")


@login_required
def task_mng(request):
    
    if request.method == "POST" and "create_task" in request.POST:
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

    
    if request.method == "POST" and "edit" in request.POST:
        task_id = request.POST.get("task_id")
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        update_task = Tasks.objects.get(id = task_id)
        update_task.title = title
        update_task.description = description
        update_task.priority = priority
        update_task.due_date = due_date
        update_task.save()
        
        messages.success(request, f"{update_task.title} is updated !")
        return redirect("tasks:manage")

    if request.method == "POST" and "delete_task" in request.POST:
        task_id = request.POST.get("task_id")
        delete_task = Tasks.objects.get(id = task_id)

        delete_task.delete()
        messages.success(request, f"{delete_task.title} is delete !")
        return redirect("tasks:manage")

    return render(request, "manage.html")



@login_required
def profile_page(request):

    if request.method == "POST" and "detail_update" in request.POST:
        request.user.first_name = request.POST.get("full_name").split(" ")[0].strip()
        request.user.last_name = request.POST.get("full_name").split(" ")[1].strip()
        request.user.username = request.POST.get("email")
        request.user.save()

        messages.success(request, "Your profile detals changed !")
        return redirect("tasks:profile")

    return render(request, "profile.html")