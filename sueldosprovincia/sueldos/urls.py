from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index.as_view(),name='index'),
    path('iniciarSesion/', LoginFormView.as_view(),name='login'),
    path('CerrarSession/', CerrarSession,name='CerrarSession'),
    path('home/', home.as_view(),name='home'),
]