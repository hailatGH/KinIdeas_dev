from core.settings import MEDIA_ROOT
from django.db import models
from django.forms import DurationField
from django.utils.translation import gettext_lazy as _
from . import validators

def artists_cover_images(instance, filename):
    return '/'.join(['artists_cover_images', str(instance.artist_name), filename])
    # The directory arrangment will be [media/artists_cover_images/{artist_name}/{filename}]

def albums_cover_images(instance, filename):
    return '/'.join(['albums_cover_images', str(instance.album_name), filename])
    # The directory arrangment will be [media/albums_cover_images/{album_name}/{filename}]

def track_files(instance, filename):
    return '/'.join(['track_files', str(instance.track_name), filename])
    # The directory arrangment will be [media/track_files/{track_name}/{filename}]

class Artist(models.Model):
    
    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['id']

    artist_name = models.CharField(max_length=50 ,default=_("unknown"),null=False ,blank=False)
    artist_avatar = models.ImageField(upload_to=artists_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=100, null=True, blank=True)
    artist_description = models.TextField(max_length=100, blank=True, null=True)
    user =  models.IntegerField(default=0)

    def __str__(self):
        return '%d: %s' % (self.pk, self.artist_name)


class Album(models.Model):
    
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['id']

    album_name = models.CharField(max_length=50,default='Collections',null=False , blank= False)
    album_cover = models.ImageField(upload_to=albums_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=100)
    album_description = models.TextField(max_length=100, blank=True, null=True)
    album_release_date=models.DateTimeField(auto_now_add=True,)
    artist = models.ForeignKey(Artist, default=0, related_name='albums', on_delete=models.DO_NOTHING)
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.album_name)

class Genre(models.Model):

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")
        ordering = ['id']

    genre_name = models.CharField(max_length=120,default='Other',null=False , blank= False)
    genre_description = models.TextField(blank=True, null=True, max_length=300)
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.genre_name)

class Track(models.Model):
    
    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['id']

    track_name = models.CharField(max_length=120,default='Unknown_track',null=False , blank= False)
    track_genre = models.ForeignKey(Genre, default=0, related_name='track', on_delete=models.DO_NOTHING)
    track_description = models.TextField(blank=True, null=True, max_length=100)
    track_file = models.FileField(upload_to=track_files, validators=[validators.validate_track_extension], null=True)
    album = models.ForeignKey(Album, default=0, related_name='tracks', on_delete=models.DO_NOTHING)
    duration=DurationField()
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.track_name)