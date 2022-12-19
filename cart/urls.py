from django.urls import path, include
from .views import CartView

urlpatterns = [
    path('add/<int:id>/', CartView.as_view(), name='cart-add'),

]