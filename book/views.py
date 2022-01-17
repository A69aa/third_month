from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def book_all(request):
    books = models.Book.objects.all()
    return render(request, "book_list.html", {'books': books})


def book_deteil(request, id):
    book = get_object_or_404(models.Book, id = id)
    return render(request, "book_deteil.html", {'book': book})

def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html',{'form': form})

