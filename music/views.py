from django.shortcuts import render, redirect
from .models import Album
from music.forms import AlbumForm
# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

def create_album(request):
    if request.method == 'POST':
        # if user is submitting the form
        form = AlbumForm(request.POST)
        # form is the filled out ("bound")
        # form with uer data
        if form.is_valid():
            #django checks if the form is valid (filled out with no errors)
            album = form.save()
            return redirect("home")
    else:
        form = AlbumForm()

    return render(request, 'music/create_album.html', {'form': form})