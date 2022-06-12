from django.forms import ModelForm
from django import forms
from .models import *

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

class TfcForm(ModelForm):
    class Meta:
        model = Project_big
        fields = '__all__'

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class ProjectSmallForm(ModelForm):
    class Meta:
        model = Project_small
        fields = '__all__'