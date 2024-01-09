from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Создан"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Изменён"))
    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [('T','текстовый ответ'), ('SQ','одиночный ответ'), ('PQ','варианты ответов')]
    text = models.TextField(verbose_name=_("Вопрос"))
    question_type = models.CharField(choices=QUESTION_TYPES, max_length=2, verbose_name=_('тип вопроса'))
    correct_answer = models.TextField(verbose_name=_('правильный ответ'))
    test = models.ForeignKey('general.Test', on_delete=models.CASCADE, default=None, null=True, related_name='questions', verbose_name='тест')
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey('general.Question', on_delete=models.CASCADE, verbose_name=_('вопрос'))
    text = models.TextField(verbose_name=_('текст варианта'))
    is_correct = models.BooleanField(default=False, verbose_name=_('правильный ответ'))

class UserAnswer(models.Model):
    question = models.ForeignKey('general.Question', on_delete=models.CASCADE, verbose_name=_('вопрос'))
    text_answer = models.TextField(null=True, blank=True, verbose_name=_('текстовый ответ'))
    choice_answer = models.ManyToManyField('general.Choice', blank=True, verbose_name=_('варианты ответа'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Создан"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Изменён"))
    