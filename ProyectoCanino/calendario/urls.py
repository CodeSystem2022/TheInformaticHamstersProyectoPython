from django.urls import path
from . import views

app_name = 'calendario'
urlpatterns = [
    path('index/', views.index, name='index'),
]
