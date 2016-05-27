from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

from books.models import Publisher, Author, Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term next time. DEAD ENDDD')
