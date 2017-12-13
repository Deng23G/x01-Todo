from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(
        deadline_date__lte=timezone.now()).order_by('deadline_date')
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_edit(request):
    form = TodoForm()
    return render(request, 'todo_edit.html', {'form': form})
