from django.forms import ModelForm
from django import forms
from .models import Post, Quizz, Question, Answer

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {            
            'title': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'min-height: 50px; min-width: 100px;', 
            'placeholder': 'titulo do comentario'}),

            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value':'', 'id':'user',
                'type':'hidden'
            }),

            'body' : forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'min-height: 200px; min-width: 100px;', 
            'placeholder': 'comentario'  
            })
        }

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

    # ferramentas
        widgets = {            
            'title': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'min-height: 50px; min-width: 100px;', 
            'placeholder': 'titulo do Quizz'}),

            'questions': forms.Select(attrs={
                'class': 'form-control',
            }),

            'user': forms.Select(attrs={
                'class': 'form-control',
            })
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    # ferramentas
    widgets = {            
        'title': forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-height: 50px; min-width: 100px;', 
        'placeholder': 'titulo da Pergunta'}),

        'questions': forms.Select(attrs={
                'class': 'form-control',
            }),

        

        'user': forms.Select(attrs={
                'class': 'form-control',
            }),

        'answers': forms.Select(attrs={
                'class': 'form-control',
            })
        }

