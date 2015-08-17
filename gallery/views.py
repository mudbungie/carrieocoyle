from django.shortcuts import render, get_object_or_404
from gallery.models import Piece

def index(request):
    # show all of the published art pieces
    pieces = Piece.objects.filter(published=True)
    return render(request, 'gallery/index.html', {'posts':posts})

def piece(request, slug):
    # pull up the individual piece
    piece = get_object_or_404(Post, slug=slug)
    return render(render, 'gallery/post.html', {'post':post})
