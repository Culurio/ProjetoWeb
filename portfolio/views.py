# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from multiprocessing import AuthenticationError
import datetime
from portfolio.forms import *
from matplotlib import pyplot as plt


from portfolio.models import *

def home_page_view(request):
    local = 'Lisboa'

    context = {
        'local': local,
    }
    return render(request, 'portfolio/home.html', context)

def licenciatura_page_view(request):
    context = {
        'cadeiras':Subject.objects.all().order_by('rank','year','semester')[:3],
    }
    return render(request, 'portfolio/licenciatura.html',context)

@login_required
def view_edit_subject(request, post_id):

    post = Subject.objects.get(id=post_id)
    form = SubjectForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/licenciatura_edit.html', context)

@login_required
def view_add_subject(request):
    form = SubjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form,}
    return render(request, 'portfolio/licenciatura_add.html', context)

@login_required
def view_delete_subject(request, project_id):

    subject = Subject.objects.get(id=project_id)
    subject.delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))

@login_required
def view_edit_project(request, post_id):

    post = Project_small.objects.get(id=post_id)
    form = ProjectSmallForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/project_edit.html', context)

@login_required
def view_add_project(request):
    form = ProjectSmallForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form,}
    return render(request, 'portfolio/project_add.html', context)

@login_required
def view_delete_project(request, project_id):

    project_small = Project_small.objects.get(id=project_id)
    project_small.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

@login_required
def view_edit_tfc(request, post_id):

    post = Project_big.objects.get(id=post_id)
    form = TfcForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/tfc_edit.html', context)

@login_required
def view_add_tfc(request):
    form = TfcForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form,}
    return render(request, 'portfolio/tfc_add.html', context)

@login_required
def view_delete_tfc(request, project_id):

    project_big = Project_big.objects.get(id=project_id)
    project_big.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

def projects_page_view(request):
    context = {
        'projects_small':Project_small.objects.all()[:3],
        'projects_big':Project_big.objects.all()[:6],
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
    
    form = PostForm(request.POST or None, request.FILES)

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
    form = PostForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/blog_edit.html', context)

@login_required
def view_delete_tarefa(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def desenha_grafico_resultados():
    participants = sorted(Quizz.objects.all(), key=lambda t: t.points, reverse=True)     
    names = []     
    points = []     
    for pt in participants:         
        names.append(pt.name +" "+pt.surname)         
        points.append(pt.points)     
        plt.barh(names, points)     
        plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')


def calculate_quizz(request):
    score = 0
    creator = request.POST.get('creator_name')
    city = request.POST.get('cname')
    framework = request.POST.get('framework')
    page_color = request.POST.get('page_color')
    print(page_color)
    if creator == "claudio" :
        score += 10
    if city == "Barreiro" :
        score += 10
    if framework.lower() == "django" :
        score += 15
    if page_color == "#f6b73c" :
        score += 15
    return score


def view_quizz(request):
    quizz = Quizz.objects.all()
    context = {'quizz': quizz}
    if request.method == 'POST':
        n = request.POST.get('user_fname')
        a = request.POST.get('user_lname')
        p = calculate_quizz(request)
        r = Quizz(name=n, surname=a, points=p)
        r.save()
        desenha_grafico_resultados()
    return render(request, 'portfolio/quizz.html',context)


def api_page_view(request):
    local = 'Lisboa'

    context = {
        'local': local,
    }
    return render(request, 'portfolio/api.html', context)