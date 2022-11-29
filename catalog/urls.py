from django.urls import path, include
from .views import IndexView

# '' - домашнаяя (главная) страница
# books/ - список всех книг
# authors/ - все авторы
# book/<id> - детальная инофрмация книги
# author/<id> - детальная инофрмация автора

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index')
]

