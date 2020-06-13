from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, db_index=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.pk)])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=255)

    def __str__(self):
        return self.review[:50]

