from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#What is model in django
    #Field: Column in the database table
    #Attribute: Represents a row in the table
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    #If you use {Listname}.create(text, complete) --> This implicit says that the todolist attribute = Listname
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text