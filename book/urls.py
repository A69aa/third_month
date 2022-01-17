from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.book_all, name='book_all'),
    path('books/<int:id>/', views.book_deteil, name='book_deteil'),
    path('add-book/',views.add_book, name='add-book'),
]