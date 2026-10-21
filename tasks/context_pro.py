from .models import Tasks

def tasks(request):
    context = {
        "tasks": Tasks.objects.filter(user_id=request.user.id).all()
    }
    return context