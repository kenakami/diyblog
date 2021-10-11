from django.contrib import admin

# Register your models here.

from .models import Post, Comment, Author

# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Author)

class CommentInline(admin.TabularInline):
    model = Comment

# Register the Admin classes for Book using the decorator
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'title')
    list_filter = ('author', 'date')
    inlines = [CommentInline]
    pass

# Register the Admin classes for Book using the decorator
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'post', 'content')
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    pass

