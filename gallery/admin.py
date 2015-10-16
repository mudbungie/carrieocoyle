from django.contrib import admin
from .models import Piece

class PieceAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = []
    search_fields = []
    date_hierarchy = 'created'
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Piece, PieceAdmin)
