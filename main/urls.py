from django.urls import path
from . import views

# set the app name
app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('add-event/', views.add_event, name="add_event"),
    path('events/details/<slug:slug>', views.details, name="details"),
    path('events/edit-event/<slug:slug>', views.edit_event, name="edit_event"),
    path('events/add-task/<slug:slug>', views.add_task, name="add_task")
]