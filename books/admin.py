# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publication_date','author','price','pages','book_type')

admin.site.register(Book, BookAdmin)
# Register your models here.
