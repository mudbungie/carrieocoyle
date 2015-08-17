from django.contrib import admin
from gallery.models import Piece

# administration for the gallery
class PieceAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = []
    search_fields = []
    date_hierarchy = 'created'
    # put the save buttons on the top of the form
    save_on_top = True
    # prepopulate the slug with the title
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Piece, PieceAdmin)
