from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    pic=models.ImageField(blank=True, null=True, upload_to='book_image')


# Create your models here.
class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date =  models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'