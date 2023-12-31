"""
URL configuration for music_sharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music_app.views import home, register
#from django.contrib.auth.views import ProfileView
#from music_app.views import profile_view
from music_app.views import song_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('music_app.urls')),
    path('register/', register, name='register'),
    path('', home, name='home' ),
    #path('accounts/profile/', ProfileView.as_view(), name='profile'),
    #path('accounts/profile/', profile_view, name='profile'),
    #path('upload/', upload_song, name='upload_song'),
    path('songs/', song_list, name='song_list'),
    
    
    
    
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
