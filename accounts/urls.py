from django.urls import path, include
from .views import SignUP


urlpatterns = [
    path('SignUp/', SignUP.as_view(), name='accounts-SignUp')

]
