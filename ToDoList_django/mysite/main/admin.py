from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.

#This gives the admin to have access to the databse we're working on 
#You can check the database through the admin page
admin.site.register(ToDoList)
admin.site.register(Item)