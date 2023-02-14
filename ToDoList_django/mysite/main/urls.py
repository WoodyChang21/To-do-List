#Define the parth to different web pages
#The urls to go to cdifferent views

from django.urls import path
from . import views

urlpatterns = [
    #this path variable "name" into views.index
    path("<int:id>", views.index, name="index"),
    path("", views.view, name="home"),
    path("view/", views.view, name="view"),
]