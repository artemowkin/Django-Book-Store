from django.urls import path

from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView,
    BookDeleteView, AddReviewView, BookSearchView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('search/', BookSearchView.as_view(), name='book_search'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<uuid:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<uuid:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<uuid:pk>/add_review/', AddReviewView.as_view(),
         name='book_add_review'),
]
