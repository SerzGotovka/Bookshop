from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cart
from catalog.models import Book
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




class CartView(TemplateView):

    @method_decorator(login_required)
    def get(self, request, id):
        book = Book.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart.products.add(book)

        return redirect('catalog-index')


class CartDelete(TemplateView):
    @method_decorator(login_required)
    def get(self, request, id):
        cart = Cart.objects.get(user=request.user)
        cart.products.set(cart.products.exclude(id=id))

        return redirect('catalog-index')


class CartDeleteAll(TemplateView):
    @method_decorator(login_required)
    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart.products.clear()

        return redirect('catalog-index')



class BuyView(TemplateView):
    template_name = 'cart/buy.html'

    def get(self, request):
        return render(request, self.template_name)




