#from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music_files/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    allowed_emails = models.TextField(blank=True)

    def is_accessible(self, email):
        if self.visibility == MusicFile.PUBLIC:
            return True
        elif self.visibility == MusicFile.PRIVATE and self.user.email == email:
            return True
        elif (
            self.visibility == MusicFile.PROTECTED and
            email in self.allowed_emails.split(',')
        ):
            return True
        return False

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to="documents")

    def __str__(self):
        return self.title  
    
    #class Meta:
        db_tables='Song' 
    
    

