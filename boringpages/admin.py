from django.contrib import admin
from .models import TextPage

class TextPageAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(TextPage, TextPageAdmin)
