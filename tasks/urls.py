from django.urls import path
from .views import home_page, task_mng, profile_page


app_name = "tasks"



urlpatterns = [
    path("", home_page, name="home"),
    path("manage/", task_mng, name="manage"),
    path("profile/", profile_page, name="profile"),
]