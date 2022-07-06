from core.settings import MEDIA_ROOT
from django.db import models
from django.forms import DurationField
from django.utils.translation import gettext_lazy as _
from . import validators

def writers_cover_images(instance, filename):
    return '/'.join(['writers_cover_images', str(instance.writer_name), filename])
    # The directory arrangment will be [media/writers_cover_images/{writer_name}/{filename}]

def narrators_cover_images(instance, filename):
    return '/'.join(['narrators_cover_images', str(instance.narrator_name), filename])
    # The directory arrangment will be [media/narrators_cover_images/{narrator_name}/{filename}]

def books_cover_images(instance, filename):
    return '/'.join(['books_cover_images', str(instance.book_name), filename])
    # The directory arrangment will be [media/books_cover_images/{book_name}/{filename}]

def book_categorys_cover_images(instance, filename):
    return '/'.join(['book_categorys_cover_images', str(instance.book_category_title), filename])
    # The directory arrangment will be [media/books_cover_images/{book_name}/{filename}]

def chapter_files(instance, filename):
    return '/'.join(['chapter_files', str(instance.chapter_name), filename])
    # The directory arrangment will be [media/chapter_files/{chapter_name}/{filename}]

class Writer(models.Model):
    
    class Meta:
        verbose_name = _("Writer")
        verbose_name_plural = _("Writers")
        ordering = ['id']

    writer_name = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    writer_title = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    writer_cover = models.ImageField(upload_to=writers_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    writer_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.writer_name)

class Narrator(models.Model):
    
    class Meta:
        verbose_name = _("Narrator")
        verbose_name_plural = _("Narratores")
        ordering = ['id']

    narrator_name = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    narrator_title = models.CharField(max_length=100, default=_("unknown"), null=False, blank=False)
    narrator_cover = models.ImageField(upload_to=narrators_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    narrator_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d: %s' % (self.pk, self.narrator_name)

class BookCategory(models.Model):

    class Meta:
        verbose_name = _("BookCategory")
        verbose_name_plural = _("BookCategories")
        ordering = ['id']

    book_category_title = models.CharField(max_length=100, default='Other', null=False, blank=False)
    book_category_cover = models.ImageField(upload_to=book_categorys_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    book_category_description = models.TextField(max_length=1023, blank=True, null=True)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.book_category_title)

class Book(models.Model):
    
    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ['id']

    book_title = models.CharField(max_length=100, default='Collections', null=False, blank= False)
    book_cover = models.ImageField(upload_to=books_cover_images, validators=[validators.validate_image_extension], height_field=None, width_field=None, max_length=1023, null=False, blank=False)
    book_description = models.TextField(max_length=1023, blank=True, null=True)
    writer_id = models.ForeignKey(Writer, default=0, related_name='books_w', on_delete=models.DO_NOTHING)
    narrator_id = models.ForeignKey(Narrator, default=0, related_name='books_n', on_delete=models.DO_NOTHING)
    book_category_id = models.ForeignKey(BookCategory, default=0, related_name='books_c', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.book_title)

class Chapter(models.Model):
    
    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapter")
        ordering = ['id']

    chapter_title = models.CharField(max_length=100, default='Unknown_chapter', null=False, blank=False)
    chapter_description = models.TextField(blank=True, null=True, max_length=100)
    chapter_file = models.FileField(upload_to=chapter_files, validators=[validators.validate_track_extension], null=False, blank=False)
    chapter_status = models.BooleanField(default=False)
    chapter_release_date = models.DateTimeField()
    book_id = models.ForeignKey(Book, default=0, related_name='chapters', on_delete=models.DO_NOTHING)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.chapter_title)