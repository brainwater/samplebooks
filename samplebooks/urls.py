from django.urls import path, re_path
from samplebooks import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('authorsearch/<str:author_name>/', views.author_search, name='author_search'),
    path('bookdetail/<str:book_id>/', views.book_detail, name='book_detail'),
]
