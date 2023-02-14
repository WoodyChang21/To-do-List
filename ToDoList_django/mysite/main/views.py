from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist_set.all():

    # {"save":["save"], "c1":["clicked"]} --> This is what post response will look like {name of the tag: value of the tag}
        if response.method=="POST":
            #This contains all the information you made in the webpage (in dictionary form)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    #This takes care the checkbox
                    if response.POST.get("c"+str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            # This takes care of the new item
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt)>2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
            #This takes care of delete
            for item in ls.item_set.all():
                if response.POST.get("t"+str(item.id))=="delete":
                    #Delete the item in that to do list
                    item_to_delete = ls.item_set.get(id=item.id)
                    item_to_delete.delete()
        
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html",{})


def view(response):
    if response.method=="POST":
        form = CreateNewList(response.POST)
        if form.is_valid() and response.POST.get("create")=="create":
            n = form.cleaned_data["name"]
            response.user.todolist_set.create(name=n)
        for todolist in response.user.todolist_set.all():
                if response.POST.get("t"+str(todolist.id))=="delete":
                    #Delete the todolist for the user
                    list_to_delete = response.user.todolist_set.get(id=todolist.id)
                    list_to_delete.delete()
        
    else: #Get method, it gets to here when you just started the web page
        form = CreateNewList()
    return render(response, "main/view.html", {"form":form})