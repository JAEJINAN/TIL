from django.contrib import admin
from .models import Question

# Register your models here.

# admin창에서 질문을 검색할 수 있게 해준다.


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
