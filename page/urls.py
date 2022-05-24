from django.urls import path
from .viewshome import home
from .viewsabout import aboutpage
from .viewsaccount import signin

urlpatterns = [
    path('', home),
    path('about/', aboutpage),
    path('account/', signin)
]
