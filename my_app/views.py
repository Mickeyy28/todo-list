from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_app.models import *
# Create your views here.


def home(request):
    context = {'page': 'home page', 'logged': False}
    return render(request, 'home.html', context)


def contact(request):
    contact_obj = Contact.objects.all()
    print(contact_obj)
    context = {'page': 'contact page', 'contacts': 'contact_obj'}
    return render(request, 'contact.html', context)


def about(request):
    context = {'page': 'about page'}
    return render(request, 'about.html', context)


def dynamic(request, id):
    context = {'page': 'dynamic page'}
    return render(request, 'dynamic.html', context)


def todo(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        print(todo)
        if todo is not None:
            todo_obj = Todo(todo_name=todo)
            todo_obj.save()
        return redirect('/todo/')
    todoss = Todo.objects.all()
    context = {'todos': todoss}
    return render(request, 'todo.html', context)


def mark_as_complete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.is_complete = True
        todo.save()
    except Todo.DoesNotExist:
        pass
    return redirect('todo/')


def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect('todo/')
