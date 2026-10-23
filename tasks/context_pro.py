from .models import Tasks
from django.db.models import Q

def tasks(request):
    tasks = Tasks.objects.filter(user_id=request.user.id)


    if request.method == "GET" and "filter" in request.GET:
        q = request.GET.get("q")
        status = request.GET.get("status")
        priority = request.GET.get("priority")

        if len(q) > 0:
            tasks = tasks.filter(title__icontains=q)

        if status == "open":
            tasks = tasks.filter(status=False)

        if status == "done":
            tasks = tasks.filter(status=True)

        if priority != "any":
            tasks = tasks.filter(priority=priority.strip())


    context = {
            "tasks": tasks.all(),
            "open_tasks": tasks.filter(status=False).all().count(),
            "done_tasks": tasks.filter(status=True).all().count()
    }

    return context