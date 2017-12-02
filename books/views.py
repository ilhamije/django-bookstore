# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books':books})

def book_create(request):
    form = BookForm()
    context = {'form': form}
    html_form = render_to_string('book/partial_book_create.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form':html_form})
