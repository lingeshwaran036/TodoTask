from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Task
from django.db.models import Q
    

def get_current_user(request):
    user_id = request.session.get('user_id')
    try:
        return get_object_or_404(User, id=user_id)
    except:
        return None
    return None    
    
        
def home(request):
    user = get_current_user(request)
    if not user:
        return redirect('login')
        
    tasks = Task.objects.filter(user=user)   
    return render(request, 'Home/index.html', {'tasks': tasks, 'user': user})
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'Home/login.html')
    
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        if user:
            return redirect('home')
        else:
            return redirect('register')
    return render(request, 'Home/register.html')
    
    
def add_task(request):
    user = get_current_user(request)
    if not user:
        return redirect('login')
        
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(user=user, title=title, description=description)
        if task:
            return redirect('home')
        else:
            return redirect('add_task')
    return render(request, 'Home/add_task.html')
    
    
def edit_task(request, task_id):
    user = get_current_user(request)
    if not user:
        return redirect('login')
        
    task = Task.objects.filter(id=task_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            task.title = title
        if description:
            task.description = description
        task.save()
        if task:
            return redirect('home')
        else:
            return redirect('edit_task', task_id)
    return render(request, 'Home/edit_task.html', {'task': task})
    
    
def mark_as_complete(request, task_id):
    user = get_current_user(request)
    if not user:
        return redirect('login')
        
    task = Task.objects.filter(id=task_id).first()
    task.is_completed = True
    task.save()
    return redirect('home')
    
    
def delete_task(request, task_id):
    user = get_current_user(request)
    if not user:
        return redirect('login')
        
    task = Task.objects.filter(id=task_id).first()
    task.delete()
    return redirect('home')
    
    
def logout(request):
    request.session.flush()
    return redirect('login')