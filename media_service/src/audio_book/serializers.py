from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Writer, Narrator, Book, BookCategory, Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'chapter_title',
            'chapter_description',
            'chapter_file',
            'chapter_status',
            'chapter_release_date',
            'book_id',
            'user_id',
            'created_at',
            'updated_at'
        ]

class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = [
            'id',
            'book_title',
            'book_cover',
            'book_description',
            'writer_id',
            'narrator_id',
            'book_category_id',
            'user_id',
            'created_at',
            'updated_at',
            'chapters',
        ]

class BookCategorySerializer(serializers.ModelSerializer):
    books_c = BookSerializer(many=True, required=False)

    class Meta:
        model = BookCategory
        fields = [
            'id',
            'book_category_title',
            'book_category_cover',
            'book_category_description',
            'user_id',
            'created_at',
            'updated_at',
            'books_c',
        ]

class NarratorSerializer(serializers.ModelSerializer):
    books_n = BookSerializer(many=True, required=False)
    
    class Meta:
        model = Narrator
        fields = [
            'id',
            'narrator_name',
            'narrator_title',
            'narrator_cover',
            'narrator_description',
            'user_id',
            'created_at',
            'updated_at',
            'books_n',
        ]

class WriterSerializer(serializers.ModelSerializer):
    books_w = BookSerializer(many=True, required=False)
    
    class Meta:
        model = Writer
        fields = [
            'id',
            'writer_name',
            'writer_title',
            'writer_cover',
            'writer_description',
            'user_id',
            'created_at',
            'updated_at',
            'books_w',
        ]