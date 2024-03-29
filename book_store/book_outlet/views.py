from django.db.models import Avg
from django.shortcuts import get_object_or_404, render

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    agg = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {"books": books, "num_books": num_books, "agg": agg},
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
