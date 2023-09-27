from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.
class ChoiseInLine(admin.TabularInline):
  model = Choice
  extra = 3 

class QuestionAdmin(admin.ModelAdmin):
  inilines = (ChoiseInLine)
  list_filter = ["pub_date"]
  search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)