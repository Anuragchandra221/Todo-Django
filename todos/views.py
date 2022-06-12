from unicodedata import category
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .models import Category, TodoList
# Create your views here.

def index(request):
    todolist = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        if "addTask" in request.POST:
            title = request.POST['title']
            date = str(request.POST['date'])
            category = request.POST['categories']
            Todo = TodoList(title=title,  due_date=date, category=Category.objects.get(name=category))
            try:
                Todo.save()
            except:
                return redirect(request.path)
            finally:
                return redirect(request.path)

        if "deleteTask" in request.POST:
            checked = request.POST.getlist("checkedbox")
            print(checked)
            for id in checked:
                todo = TodoList.objects.get(id=int(id))
                todo.delete()
            return redirect(request.path)

        if "addCategory" in request.POST:
            name = request.POST["name"]
            Cat = Category(name=name)
            try:
                Cat.save()
            except:
                return redirect(request.path)
            finally:
                return redirect(request.path)

        if "deleteCategory" in request.POST:
            checked = request.POST.getlist("checkedboxCat")
            for id in checked:
                Cat = Category.objects.get(id=int(id))
                Cat.delete()
            return redirect(request.path)

        
        sort = request.POST['sort']
        todolist = TodoList.objects.all().order_by(sort)
        print(sort)

    print(request.POST)

    ctx = {
        "todos": todolist,
        "categories": categories
    }
    return render(request, 'todos/index.html', ctx)