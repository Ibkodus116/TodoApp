from django.shortcuts import render, redirect

from myapp.forms import TodoForm
from .models import Todo


def mytodo (request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        enter = TodoForm(request.POST)
        if enter.is_valid():
            enter.save()
            return redirect('home')
    else:
        enter = TodoForm()
    
    return render (request, 'pages/index.html', {
        'todo': todo,
        'enter': enter
    })

