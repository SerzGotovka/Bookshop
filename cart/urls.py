from django.urls import path
from .views import CartView, BuyView, CartDelete, CartDeleteAll

urlpatterns = [
    path('add/<int:id>/', CartView.as_view(), name='cart-add'),
    path('delete/<int:id>/', CartDelete.as_view(), name='delete-book'),
    path('buy/', BuyView.as_view(), name='cart-buy'),
    path('delete/All/', CartDeleteAll.as_view(), name='delete-all')

]
