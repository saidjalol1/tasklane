from django.db import models
from django.contrib.auth.models import User



class Tasks(models.Model):
    title =models.CharField(max_length = 100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")


    def __str__(self):
        return self.title