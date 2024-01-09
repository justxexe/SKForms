# Generated by Django 4.2.7 on 2023-12-06 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст варианта')),
                ('is_correct', models.BooleanField(default=False, verbose_name='правильный ответ')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Вопрос')),
                ('question_type', models.CharField(choices=[('T', 'текстовый ответ'), ('SQ', 'одиночный ответ'), ('PQ', 'варианты ответов')], max_length=2, verbose_name='тип вопроса')),
                ('correct_answer', models.TextField(verbose_name='правильный ответ')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, null=True, verbose_name='текстовый ответ')),
                ('choice_answer', models.ManyToManyField(blank=True, to='general.choice', verbose_name='варианты ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.question', verbose_name='вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменён')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.question', verbose_name='вопрос'),
        ),
    ]
