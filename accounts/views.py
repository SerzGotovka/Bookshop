from django.shortcuts import render
from django.views.generic import TemplateView


class SignUP(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)
