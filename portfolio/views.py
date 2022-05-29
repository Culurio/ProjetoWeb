# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from multiprocessing import AuthenticationError
import datetime
from portfolio.forms import *

from portfolio.models import Subject, Teacher, Project, Post

def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local,
    }
    return render(request, 'portfolio/home.html', context)

def licenciatura_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    context = {
        'cadeiras':Subject.objects.all().order_by('year','semester')[:3],
    }
    return render(request, 'portfolio/licenciatura.html',context)

def projects_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    context = {
        'projects':Project.objects.all(),
    }
    return render(request, 'portfolio/projects.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, "portfolio/login.html",{
                'message' : "Invalid Credentials."
            })
    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
                'message': 'Foi desconetado.'
            })

def view_new_post(request):
    
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form,
        'posts': Post.objects.all().order_by('post_date')
    }
    return render(request, 'portfolio/blog.html', context)

@login_required
def view_edit_post(request, post_id):

    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/blog_edit.html', context)

def view_delete_tarefa(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


@login_required
def view_quizz(request):

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:quizz'))

    context = {'form': form,
        'quizzes': Quizz.objects.all()
    }
    return render(request, 'portfolio/quizz.html', context)