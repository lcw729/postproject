from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    chaewons = Blog.objects
    return render(request, 'home.html', {"chaewons": chaewons})

def detail(request, chaewon_id):
    detail_page = get_object_or_404(Blog, pk=chaewon_id)
    return render(request, 'detail.html', {'detail_page': detail_page})

def new(request):
    return render(request, 'new.html')

def create(request):
    chaewon = Blog()
    chaewon.title = request.POST['title']
    chaewon.body = request.POST['body']
    chaewon.pub_date = timezone.datetime.now()
    chaewon.save()
    return redirect('/blog/'+str(chaewon.id))

def delete(request, chaewon_id):
    destroy = get_object_or_404(Blog, pk=chaewon_id)
    destroy.delete()
    return redirect('home')

def update(request, chaewon_id):
    text = get_object_or_404(Blog, pk=chaewon_id)
    return render(request, 'update.html', {'text': text})

def edit(request, chaewon_id):
    edit = Blog.objects.get(pk=chaewon_id)
    edit.title = request.POST['title']
    edit.body = request.POST['body']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')