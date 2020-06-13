from django.urls import reverse_lazy
from django.conf import settings
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)

from .models import Book, Review


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['stripe_amount'] = str(
            self.get_object().price).replace('.', '')
        return context


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_create.html'
    permission_required = 'books.add_book'


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    context_object_name = 'book'
    template_name = 'books/book_update.html'
    permission_required = 'books.change_book'


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_delete.html'
    permission_required = 'books.delete_book'
    success_url = reverse_lazy('book_list')


class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('review',)
    template_name = 'books/add_review.html'
    login_url = reverse_lazy('account_login')

    def setup(self, request, *args, **kwargs):
        self.book = Book.objects.get(pk=kwargs.get('pk'))
        super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.book
        return context

    def get_success_url(self):
        return self.book.get_absolute_url()

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.book = self.book
        return super().form_valid(form)


class BookSearchView(ListView):
    model = Book
    context_object_name = 'search_results'
    template_name = 'books/search.html'

    def setup(self, request, *args, **kwargs):
        self.query = request.GET.get('query')
        super().setup(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(
            Q(title__icontains=self.query) | Q(author__icontains=self.query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context
