from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('subject_edit/<int:post_id>',views.view_edit_subject,name='subject_edit'),
    path('subject_add',views.view_add_subject,name='subject_add'),
    path('delete_licenciatura/<int:post_id>',views.view_delete_subject,name='licenciatura_delete'),
    path('projetos', views.projects_page_view, name='projetos'),
    path('project_edit/<int:post_id>',views.view_edit_project,name='project_edit'),
    path('project_add',views.view_add_project,name='project_add'),
    path('delete_project/<int:project_id>', views.view_delete_project, name='delete_project'),
    path('tfc_edit/<int:post_id>',views.view_edit_tfc,name='tfc_edit'),
    path('tfc_add',views.view_add_tfc,name='tfc_add'),
    path('delete_tfc/<int:project_id>', views.view_delete_tfc, name='delete_tfc'),
    path('blog', views.view_new_post, name='blog'),
    path('blog_edit/<int:post_id>', views.view_edit_post, name='blog_edit'),
    path('delete/<int:post_id>', views.view_delete_tarefa, name='delete_blog'),
    path('quizz', views.view_quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.view_logout, name='logout'),
]