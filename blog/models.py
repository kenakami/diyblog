from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('date', auto_now_add=True)
    title = models.CharField(max_length=200, help_text='Enter the title of your post')
    content = models.TextField(max_length=8000, help_text='Enter the content of your post')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.author} ({self.date}) - {self.title}'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('date', auto_now_add=True)
    content = models.TextField(max_length=2000, help_text='Enter the content of your comment')
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.user} ({self.date}) : {self.content}'

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=8000, help_text='Enter your bio')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
