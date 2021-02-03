from django.contrib import admin
from . import models


# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['created', 'question', 'choice']


admin.site.register(models.Choice)
admin.site.register(models.Question)
admin.site.register(models.Answer, AnswerAdmin)
