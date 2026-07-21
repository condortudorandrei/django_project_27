from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book


# Create your views here.

# functions that manage our web pages.

def home(request: HttpRequest):
    return HttpResponse('Ai carte, ai parte')


# function-based view
# CRUD: create, read, update, delete


def list_books(request: HttpRequest):
    # trebuie sa listam cartile din baza de date.
    # accesam cartiile
    # QuerySet

    sort = request.GET.get("sort")
    books = Book.objects.all().order_by("pk")

    if sort == "asc":
        books = Book.objects.all().order_by("title")
    if sort == "desc":
        books = Book.objects.all().order_by("-title")
    if sort == "default":
        books = Book.objects.all().order_by("pk")

    return render(request, 'books/home.html', context={"books": books})


def create_book(request: HttpRequest):
    if request.method == 'POST':
        # detaliile book-ului care au fost trimise de form folosind HTTP POST request, se afla in request.POST ca un dictionar.
        book_instance = BookForm(request.POST)
        if book_instance.is_valid():
            # aici se creeaza un book in baza de date!
            book_instance.save()
            return redirect('create_book')
        # return HttpResponse('ÜBERRASCHUNG MOTHERFUCKER!')
    else:
        # in cazul asta, request-ul poate fi GET, PUT, PATCH, DELETE, etc
        form = BookForm()
        list1 = [10, 20, 30, 40, 50]
        return render(request, 'books/book_form.html', context={'form': form, 'list1': list1})


def delete_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    else:
        return render(request, 'books/book_confirm_delete.html', context={'book': book})


def update_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    # book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # detaliile book-ului care au fost trimise de form folosind HTTP POST request, se afla in request.POST ca un dictionar.
        book_instance = BookForm(request.POST, instance=book)
        if book_instance.is_valid():
            # aici se updateaza un book in baza de date!
            book_instance.save()
            return redirect('home')
        # return HttpResponse('ÜBERRASCHUNG MOTHERFUCKER!')
    else:
        # in cazul asta, request-ul poate fi GET, PUT, PATCH, DELETE, etc
        form = BookForm(instance=book)
        list1 = [10, 20, 30, 40, 50]
        return render(request, 'books/update_book_form.html', context={'form': form})
