from django.urls import path
from .import views

urlpatterns = [
    path('url-loop/', views.url_list_view, name='show-url-list'),
]