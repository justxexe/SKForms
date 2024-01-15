from django.contrib import admin
from .models import Test, Question, Choice, UserAnswer

admin.site.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'questions']
    search_fields = ['title']

admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'question_type', 'test']
    list_filter = ['question_type', 'test']

admin.site.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    list_filter = ['question']

admin.site.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text_answer', 'number_answer']
    list_filter = ['question']
