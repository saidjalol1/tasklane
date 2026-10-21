from django.urls import path
from .views import home_page, task_mng


app_name = "tasks"



urlpatterns = [
    path("", home_page, name="home"),
    path("manage/", task_mng, name="manage"),
]