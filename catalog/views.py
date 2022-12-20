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


class AuthorsView(TemplateView):
    template_name = 'catalog/authors.html'

    def get(self, request):
        authors = Author.objects.all()
        params = {
            'authors': authors
        }
        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = 'catalog/book.html'

    def get(self, request, id):
        get = Book.objects.get(id=id)
        book = get
        params = {
            'book': book
        }
        return render(request, self.template_name, params)


class AuthorView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, first_name, last_name):
        author = Author.objects.get(first_name=first_name, last_name=last_name)
        books = Book.objects.filter(author=author)
        params = {
            'books': books
        }
        return render(request, self.template_name, params)

class GenresView(TemplateView):
    template_name = 'catalog/genres.html'

    def get(self, request):
        genres = Genre.objects.all

        params = {
            'genres': genres
        }
        return render(request, self.template_name, params)


class GenreView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, name):
        genre = Genre.objects.get(name=name)
        books = Book.objects.filter(genre=genre)
        params = {
            'genre': genre,
            'books': books
        }
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = 'catalog/index.html'

    def post(self, request):

        content = request.POST['content']
        # search_author = Author.objects.filter(last_name=content)
        books_by_title = Book.objects.filter(title__icontains=content)
        # books_by_author = Book.objects.filter(author=content)
        books_by_summary = Book.objects.filter(summary__icontains=content)
        result = books_by_title.union(books_by_summary, all=False)

        params = {
            'books': result
        }
        return render(request, self.template_name, params)


