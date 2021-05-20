from django import forms
from django.forms import Form, ModelForm
from samplebooks_site.settings import AUTHOR_MAX_LENGTH
from samplebooks.models import Review

class AuthorSearchForm(forms.Form):
    # TODO: An author's name may be longer than an arbitrary length.
    # Make sure the product owner approves having a maximum length, or change this to a TextField
    author_name = forms.CharField(label='Author Name', max_length=AUTHOR_MAX_LENGTH)

class BookReviewForm(Form):
    content = forms.CharField(label='Review Content')
