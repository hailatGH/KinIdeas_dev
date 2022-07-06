from django.contrib import admin

from .models import Writer, Narrator, BookCategory, Book, Chapter

# Register your models here.

admin.site.register(Writer)
admin.site.register(Narrator)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Chapter)