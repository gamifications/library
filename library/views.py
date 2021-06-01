from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect,render


from library.models import Book, Borrower

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class BookListView(generic.list.ListView):
    """Return list of all books in library"""
    model = Book

@login_required
def check_out(request, pk):
    """Borrow A Book"""
    book = Book.objects.get(id=pk)
    if book.available_copies<1:
        messages.error(request, 'Out of stock.')
    else:
        _,created = Borrower.objects.get_or_create(user=request.user, book = book)
        if created:
            # reduce stock
            book.available_copies = book.available_copies - 1
            book.save()
            messages.success(request, f'Congratulations! Book {book.title} has orderd successfully.')
        else:
            messages.error(request, f'Already ordered this book {book.title}.')
    return redirect('library:my-books')

@login_required
def check_in(request,pk):
    """Return A Book"""
    borr = Borrower.objects.get(user=request.user, book_id = pk)
    borr.book.available_copies = borr.book.available_copies + 1
    borr.book.save()
    borr.delete()
    messages.success(request, f'Book {borr.book.title} has been returned.')
    return redirect('library:my-books')

@login_required
def my_books(request):
    user=Borrower.objects.filter(user=request.user)
    return render(request, 'library/book_list.html', {'object_list':[b.book for b in user], 'return':True})

