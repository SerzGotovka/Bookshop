from django.urls import path, include
from .views import IndexView, BookView, AuthorsView, AuthorView, GenresView, GenreView, SearchView
from django.conf import settings
from django.conf.urls.static import static

# '' - домашнаяя (главная) страница
# books/ - список всех книг
# authors/ - все авторы
# book/<id> - детальная инофрмация книги
# author/<id> - детальная инофрмация автора

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    path('catalog/genres/', GenresView.as_view(), name='catalog-genres'),
    path('book/<int:id>/', BookView.as_view(), name='catalog-book'),
    path('catalog/<str:first_name>-<str:last_name>/', AuthorView.as_view(), name='catalog-author'),
    path('catalog/genres/<str:name>/', GenreView.as_view(), name='catalog-genre'),
    path('catalog/search/', SearchView.as_view(), name='catalog-search'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

