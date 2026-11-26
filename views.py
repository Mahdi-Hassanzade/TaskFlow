from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class Main(View,LoginRequiredMixin):
    login_url='login'
    def get(self,request):
        if request.user.is_authenticated:
            all_tasks = TaskModel.objects.filter(user=request.user)

            model = all_tasks.exclude( status='completed').order_by('-priority', '-created_at')

        else:
            all_tasks = TaskModel.objects.none()
            model = TaskModel.objects.none()

        search = request.GET.get('search', '')
        tasks = model

        if search:
            tasks = tasks.filter(title__icontains=search)

        all_task_count = all_tasks.count()
        pending_count = all_tasks.filter(status='pending').count()
        progress_count = all_tasks.filter(status='in progress').count()
        completed_count = all_tasks.filter(status='completed').count()
        low_count = all_tasks.filter(priority=1).count()
        medium_count = all_tasks.filter(priority=2).count()
        high_count = all_tasks.filter(priority=3).count()

        paginator = Paginator(tasks, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'index.html', {'models': page_obj,'search':
        search,'pending': pending_count,'progress': progress_count,'completed': completed_count,'all_count':
        all_task_count,'low_count': low_count,'medium_count': medium_count,'high_count': high_count,'page': page_obj})

class Update(View):
    def get(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)
        task_form=TaskForm(instance=model)
        if task_form.is_valid():
            save_form=task_form.save(commit=False)
            task_form.user=request.user
            save_form.save()
            return redirect('/')
        return render(request,'update.html',{"form":task_form})

    def post(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)
        task_form=TaskForm(request.POST,instance=model)
        if task_form.is_valid():
            save_form = task_form.save(commit=False)
            task_form.user = request.user
            save_form.save()
            return redirect('/')
        return render(request,'update.html',{"form":task_form})


class Add (LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        form=TaskForm()
        return render(request,'add.html',{"form":form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('/')

        print(form.errors)
        return render(request, 'add.html', {"form": form})

class Delete(View):
    def get(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)
        model.delete()
        return redirect('/')

    def post(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)
        model.delete()
        return redirect('/')

class Complete(View):
    def get(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)

        model.status='completed'
        model.save()
        return redirect('/')

    def post(self,request,id):
        model=get_object_or_404(TaskModel,id=id,user=request.user)

        model.status='completed'
        model.save()
        return redirect('/')
