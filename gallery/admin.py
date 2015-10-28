from django.contrib import admin
from .models import Piece
from .models import Medium

class MediumAdmin(admin.ModelAdmin):
    list_display = ['medium_name']

admin.site.register(Medium, MediumAdmin)

class PieceAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = []
    search_fields = []
    date_hierarchy = 'created'
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Piece, PieceAdmin)
