from django.contrib import admin

from .models import Writer, Narrator, Category, Book, Chapter

# Register your models here.

admin.site.register(Writer)
admin.site.register(Narrator)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Chapter)