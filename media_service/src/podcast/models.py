from core.settings import MEDIA_ROOT
from django.db import models
from django.forms import DurationField
from django.utils.translation import gettext_lazy as _
from . import validators

def hosts_cover_images(instance, filename):
    return '/'.join(['hosts_cover_images', str(instance.host_name), filename])
    # The directory arrangment will be [media/hosts_cover_images/{host_name}/{filename}]

def seasons_cover_images(instance, filename):
    return '/'.join(['seasons_cover_images', str(instance.season_name), filename])
    # The directory arrangment will be [media/seasons_cover_images/{season_name}/{filename}]

def episode_files(instance, filename):
    return '/'.join(['episode_files', str(instance.episode_name), filename])
    # The directory arrangment will be [media/episode_files/{episode_name}/{filename}]

class Host(models.Model):
    
    class Meta:
        verbose_name = _("Host")
        verbose_name_plural = _("Hosts")
        ordering = ['id']

    host_name = models.CharField(max_length=50 ,default=_("unknown"),null=False ,blank=False)
    host_avatar = models.ImageField(upload_to=hosts_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=100, null=True, blank=True)
    host_description = models.TextField(max_length=100, blank=True, null=True)
    user =  models.IntegerField(default=0)

    def __str__(self):
        return '%d: %s' % (self.pk, self.host_name)


class Season(models.Model):
    
    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")
        ordering = ['id']

    season_name = models.CharField(max_length=50,default='Collections',null=False , blank= False)
    season_cover = models.ImageField(upload_to=hosts_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=100)
    season_description = models.TextField(max_length=100, blank=True, null=True)
    season_release_date=models.DateTimeField(auto_now_add=True,)
    host = models.ForeignKey(Host, default=0, related_name='seasons', on_delete=models.DO_NOTHING)
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.season_name)

class Category(models.Model):

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['id']

    category_name = models.CharField(max_length=120,default='Other',null=False , blank= False)
    category_description = models.TextField(blank=True, null=True, max_length=300)
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.category_name)

class Episode(models.Model):
    
    class Meta:
        verbose_name = _("Episode")
        verbose_name_plural = _("Episodes")
        ordering = ['id']

    episode_name = models.CharField(max_length=120,default='Unknown_track',null=False , blank= False)
    episode_category = models.ForeignKey(Category, default=0, related_name='episode', on_delete=models.DO_NOTHING)
    episode_description = models.TextField(blank=True, null=True, max_length=100)
    episode_file = models.FileField(upload_to=episode_files, validators=[validators.validate_track_extension], null=True)
    season = models.ForeignKey(Season, default=0, related_name='episodes', on_delete=models.DO_NOTHING)
    duration=DurationField()
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.episode_name)