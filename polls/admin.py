from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):    # StackedInline can also be used.
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject', {'fields': ['subject']}),
        ('Date Published', {'fields': ['date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('subject', 'date', 'was_published_recently')
    list_filter = ['date']
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
