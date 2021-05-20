from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from samplebooks_site.settings import GOOGLEAPI_KEY, AUTHOR_MAX_LENGTH
from samplebooks.helpers import google_search_author, google_book_details, review_list
from samplebooks.models import Book, Review
from samplebooks.forms import AuthorSearchForm, BookReviewForm
import requests


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AuthorSearchForm(request.POST)
        if form.is_valid():
            #request.session['author_name'] = form.cleaned_data['author_name']
            return redirect('author_search', author_name=form.cleaned_data['author_name'])
        else:
            # TODO: implement error handling
            pass
    else:
        authorForm = AuthorSearchForm()
    reviews = review_list(Review.objects.all())
    print(reviews)
    return render(request, 'authorsearchform.html', {'authorForm': authorForm,
                                                     'reviews': reviews,})

def author_search(request, author_name):
    if len(author_name) > AUTHOR_MAX_LENGTH:
        return HttpResponseNotFound("Author name too long")
    
    # TODO: handle request failed exception
    # TODO: handle invalid response format exception
    booklist = google_search_author(author_name)
    return render(request, 'booklist.html',
                  {'booklist': booklist,})

def book_detail(request, book_id):
    # TODO: convert from try/catch since a book not in the database isn't 'exceptional'
    try:
        db_book = Book.objects.get(google_volume_id=book_id)
        db_book_exists = True
    except Book.DoesNotExist:
        db_book = None
        db_book_exists = False
    if request.method == 'POST':
        if not db_book_exists:
            # Supposed to be atomic call to create or get book object
            db_book, created = Book.objects.get_or_create(
                google_volume_id=book_id)
            if created:
                db_book_exists = True
        reviewForm = BookReviewForm(request.POST)
        if reviewForm.is_valid():
            content = reviewForm.cleaned_data['content']
            review = Review(book=db_book, content=content)
            review.save()
    if db_book_exists:
        reviews = db_book.review_set.all()
    else:
        reviews = []
    # TODO: handle exceptions of failed request or invalid response format
    params = google_book_details(book_id)
    reviewForm = BookReviewForm()
    params['reviewForm'] = reviewForm
    params['reviews'] = reviews
    
    return render(request, 'bookdetail.html', params)

