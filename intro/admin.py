from django.contrib import admin
from .models import Person, Degrees


class DegreesInline(admin.StackedInline):
    model = Degrees
    extra = 2


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identity', {'fields': ['name', 'status', 'gender', 'age', 'religion', 'image']}),
    ]
    inlines = [DegreesInline]
    list_display = ('name', 'status', 'age')
    search_fields = ['status', 'name']


admin.site.register(Person, PersonAdmin)
