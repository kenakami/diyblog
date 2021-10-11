from django.shortcuts import render

# Create your views here.

from .models import Post, Comment, Author

def index(request):
    num_posts = Post.objects.count()
    num_comments = Comment.objects.count()
    num_authors = Author.objects.count()

    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class CommentListView(generic.ListView):
    model = Comment

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = Author

import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from blog.forms import CommentForm

@login_required
def comment(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    post = get_object_or_404(Post, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CommentForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # book_instance.due_back = form.cleaned_data['renewal_date']
            comment = Comment(user=request.user, post=post, content=form.cleaned_data['content'])
            comment.save()

            # redirect to a new URL:
            return HttpResponseRedirect(post.get_absolute_url())

    # If this is a GET (or any other method) create the default form.
    else:
        """
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
        """
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'blog/comment.html', context)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behavior
        return super(BlogCommentCreate, self).form_valid(form)


