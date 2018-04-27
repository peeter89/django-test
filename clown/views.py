from django.shortcuts import render
from .models import Author, Hashtag, Post
from django.views import generic
from django.utils import timezone
from datetime import datetime
import logging


# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_posts = Post.objects.filter(date_publish__lte=datetime.now()).count()
	num_authors = Author.objects.all().count()
	num_hashtags = Hashtag.objects.all().count()

	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'clown_index.html',
		context={'num_posts':num_posts, 'num_authors': num_authors ,'num_hashtags':num_hashtags},
	)

#Author View
class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'   # your own name for the list as a template variable
    template_name = 'clown/author-list.html'  # Specify your own template name/location
    paginate_by = 10


    def get_queryset(self):
        return Author.objects.all()[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        return context


class AuthorDetailView(generic.DetailView):
    model = Author
    

    def get_context_data(self,**kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        
        
        
        # Create any data and add it to the context
        context['num_authors_post'] = Post.objects.filter(author_id=self.kwargs['pk'],date_publish__lte=datetime.now()).count
        return context
    
#HashTag View
class HashtagListView(generic.ListView):
    model = Hashtag
    context_object_name = 'hashtag_list'   # your own name for the list as a template variable
    template_name = 'clown/hashtag-list.html'  # Specify your own template name/location
    paginate_by = 10


    def get_queryset(self):
        return Hashtag.objects.all() # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HashtagListView, self).get_context_data(**kwargs)
        return context


class HashtagDetailView(generic.DetailView):
    model = Hashtag


#Post View
class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'   # your own name for the list as a template variable
    template_name = 'clown/post-list.html'  # Specify your own template name/location
    paginate_by = 10


    def get_queryset(self):
        return Post.objects.filter(date_publish__lte=datetime.now())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PostListView, self).get_context_data(**kwargs)
        return context


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_publish__lte=datetime.now())

    