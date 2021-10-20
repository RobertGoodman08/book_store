from django.db import models
from book.models import Book





class Comment(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=150, verbose_name='Name')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']
