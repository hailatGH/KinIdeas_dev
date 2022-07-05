from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Writer, Narrator, Book, Category, Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'chapter_name',
            'chapter_description',
            'book',
            'chapter_file',
        ]

class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = [
            'id',
            'book_name',
            'book_description',
            'book_release_date',
            'book_cover',
            'writer',
            'narrator',
            'category',
            'chapters',
        ]

class CategorySerializer(serializers.ModelSerializer):
    books_c = BookSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_description',
            'books_c',
        ]

class NarratorSerializer(serializers.ModelSerializer):
    books_n = BookSerializer(many=True, required=False)
    
    class Meta:
        model = Narrator
        fields = [
            'id',
            'narrator_name',
            'narrator_avatar',
            'narrator_description',
            'books_n',
        ]

class WriterSerializer(serializers.ModelSerializer):
    books_w = BookSerializer(many=True, required=False)
    
    class Meta:
        model = Writer
        fields = [
            'id',
            'writer_name',
            'writer_avatar',
            'writer_description',
            'books_w',
        ]