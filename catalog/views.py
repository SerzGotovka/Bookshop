from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Book, Author, Genre
from cart.cart import get_cart
from django.db.models import Q



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
            'numb_genres': numb_genres,

        }
        data = get_cart(request, data)
        return render(request, self.template_name, data)


class AuthorsView(TemplateView):
    template_name = 'catalog/authors.html'

    def get(self, request):
        authors = Author.objects.all()
        params = {
            'authors': authors
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = 'catalog/book.html'

    def get(self, request, id):
        get = Book.objects.get(id=id)
        book = get
        params = {
            'book': book
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)




class AuthorView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, first_name, last_name):
        author = Author.objects.get(first_name=first_name, last_name=last_name)
        books = Book.objects.filter(author=author)
        params = {
            'books': books
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class GenresView(TemplateView):
    template_name = 'catalog/genres.html'

    def get(self, request):
        genres = Genre.objects.all

        params = {
            'genres': genres
        }
        params = get_cart(request, params)
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
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = 'catalog/index.html'

    def post(self, request):

        content = request.POST['content']

        result = Book.objects.filter(
            Q(title__icontains=content) |
            Q(summary__icontains=content) |
            Q(author__first_name__icontains=content) |
            Q(author__last_name__icontains=content)
        )

        params = {
            'books': result,

        }
        params = get_cart(request, params)
        if result:
            return render(request, self.template_name, params)
        else:
            return render(request, 'catalog/not_found.html')







