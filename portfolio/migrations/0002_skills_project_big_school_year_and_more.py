# Generated by Django 4.0.1 on 2022-06-12 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('popularity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='project_big',
            name='school_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project_small',
            name='school_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project_big',
            name='teacher',
            field=models.ManyToManyField(related_name='advisor', to='portfolio.Teacher'),
        ),
        migrations.RemoveField(
            model_name='project_small',
            name='skills',
        ),
        migrations.AlterField(
            model_name='project_small',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher', to='portfolio.Teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(blank=True, to='portfolio.Student'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project_small'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher_practice',
            field=models.ManyToManyField(related_name='practice_teacher', to='portfolio.Teacher'),
        ),
        migrations.AddField(
            model_name='project_small',
            name='skills',
            field=models.ManyToManyField(related_name='teacher', to='portfolio.Skills'),
        ),
    ]
