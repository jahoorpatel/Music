from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import MusicFile
from .models import Song
from .forms import SongForm

def Song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'upload_song.html', {'form': form})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music_app/song_list.html', {'songs': songs})

@login_required
def home(request):
    user = request.user
    user_music_files = MusicFile.objects.filter(user=user)
    public_music_files = MusicFile.objects.filter(visibility=MusicFile.PUBLIC)
    protected_music_files = MusicFile.objects.filter(
        visibility=MusicFile.PROTECTED,
        allowed_emails__contains=user.email
    )
    return render(request, 'home.html', {
        'user_music_files': user_music_files,
        'public_music_files': public_music_files,
        'protected_music_files': protected_music_files
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


