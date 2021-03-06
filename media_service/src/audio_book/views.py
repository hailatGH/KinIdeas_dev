from rest_framework import generics

from .models import Writer, Narrator, BookCategory, Book, Chapter
from .serializers import WriterSerializer, NarratorSerializer, BookCategorySerializer, BookSerializer, ChapterSerializer

# Create your views here.

class WriterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

writer_list_create_view = WriterListCreateAPIView.as_view()

class WriterDetailAPIView(generics.RetrieveAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

writer_detail_view = WriterDetailAPIView.as_view()

class WriterUpdateAPIView(generics.UpdateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

writer_update_view = WriterUpdateAPIView.as_view()

class WriterDestroyAPIView(generics.DestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

writer_destroy_view = WriterDestroyAPIView.as_view()

class NarratorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorSerializer

narrator_list_create_view = NarratorListCreateAPIView.as_view()

class NarratorDetailAPIView(generics.RetrieveAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorSerializer

narrator_detail_view = NarratorDetailAPIView.as_view()

class NarratorUpdateAPIView(generics.UpdateAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

narrator_update_view = NarratorUpdateAPIView.as_view()

class NarratorDestroyAPIView(generics.DestroyAPIView):
    queryset = Narrator.objects.all()
    serializer_class = NarratorSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

narrator_destroy_view = NarratorDestroyAPIView.as_view()

class BookCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

book_category_list_create_view = BookCategoryListCreateAPIView.as_view()

class BookCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

book_category_detail_view = BookCategoryDetailAPIView.as_view()

class BookCategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

book_category_update_view = BookCategoryUpdateAPIView.as_view()

class BookCategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

book_category_destroy_view = BookCategoryDestroyAPIView.as_view()

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_list_create_view = BookListCreateAPIView.as_view()

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_detail_view = BookDetailAPIView.as_view()

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

book_update_view = BookUpdateAPIView.as_view()

class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

book_destroy_view = BookDestroyAPIView.as_view()

class ChapterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

chapter_list_create_view = ChapterListCreateAPIView.as_view()

class ChapterDetailAPIView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

chapter_detail_view = ChapterDetailAPIView.as_view()

class ChapterUpdateAPIView(generics.UpdateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

chapter_update_view = ChapterUpdateAPIView.as_view()

class ChapterDestroyAPIView(generics.DestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

chapter_destroy_view = ChapterDestroyAPIView.as_view()