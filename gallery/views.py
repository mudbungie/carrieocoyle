from django.shortcuts import render
from gallery.models import Piece

def pieces(request):
    # show all of the published art pieces
    pieces = Piece.objects.filter(published=True).order_by('created')
    return render(request, 'gallery/gallery_layout.html', {'pieces':pieces})

def piece(request, slug):
    # just see an individual piece
    pieces = get_object_or_404(Piece, slug=slug)
    return render(render, 'gallery/post.html', {'piece':piece})

