from django.urls import include, path
from . import views

app_name='library'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('<int:pk>/borrow/', views.check_out, name='check_out'),
    path('<int:pk>/return/', views.check_in, name='check_in'),
    path('my_books/', views.my_books, name='my-books'),
]