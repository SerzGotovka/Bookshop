from django.urls import path, include
from .views import IndexView, BookView, AuthorsView, AuthorView

# '' - домашнаяя (главная) страница
# books/ - список всех книг
# authors/ - все авторы
# book/<id> - детальная инофрмация книги
# author/<id> - детальная инофрмация автора

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    path('book/<int:id>/', BookView.as_view(), name='catalog-book'),
    path('catalog/<str:first_name>-<str:last_name>/', AuthorView.as_view(), name='catalog-author')

]

