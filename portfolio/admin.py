from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(Answer)