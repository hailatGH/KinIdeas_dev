from core.settings import MEDIA_ROOT
from django.db import models
from django.utils.translation import gettext_lazy as _
from . import validators

def radio_cover_images(instance, filename):
    return '/'.join(['radio_cover_images', str(instance.station_name), filename])
    # The directory arrangment will be [media/radio_cover_images/{station_name}/{filename}]

class Radio(models.Model):
    
    class Meta:
        verbose_name = _("Radio")
        verbose_name_plural = _("Radios")
        ordering = ['id']

    station_name = models.CharField(max_length=120,default='Unknown_radio',null=False , blank= False)
    station_frequency = models.FloatField(default=0, null=False , blank= False)
    station_url = models.CharField(max_length=120, default = "", null=False , blank= False)
    station_description = models.TextField(blank=True, null=True, max_length=200)
    cover_image = models.FileField(upload_to=radio_cover_images, validators=[validators.validate_image_extension], null=True)
    user =  models.IntegerField(default=0)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.station_name)