from django.shortcuts import render, get_object_or_404
from gallery.models import Piece

def pieces(request):
    # show all of the published art pieces
    pieces = Piece.objects.filter(published=True).order_by('created')
    return render(request, 'gallery/gallery_layout.html', {'pieces':pieces})

def piece(request, slug):
    # just see an individual piece
    piece = get_object_or_404(Piece, slug=slug)
    return render(request, 'gallery/post.html', {'piece':piece})
