from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        books = Book.objects.all()
        numb_books = books.count()
        authors = Author.objects.all()
        numb_authors = authors.count()
        genres = Genre.objects.all()
        numb_genres = genres.count()
        data = {
            'books': books,
            'numb_books': numb_books,
            'authors': authors,
            'numb_authors': numb_authors,
            'genres': genres,
            'numb_genres': numb_genres
        }
        return render(request, self.template_name, data)





