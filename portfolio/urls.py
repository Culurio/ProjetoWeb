from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projects_page_view, name='projetos'),
    path('blog', views.view_new_post, name='blog'),
    path('blog_edit/<int:post_id>', views.view_edit_post, name='blog_edit'),
    path('delete/<int:post_id>', views.view_delete_tarefa, name='delete'),
    path('quizz', views.view_quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.view_logout, name='logout'),
]