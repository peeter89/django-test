from django.shortcuts import render
from .models import Author, Hashtag
from django.views import generic

# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_posts = 10
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

    def author_detail_view(request,pk):
	    try:
	        author_id=Author.objects.get(pk=pk)
	    except Author.DoesNotExist:
	        raise Http404("Author does not exist")

	    #book_id=get_object_or_404(Book, pk=pk)
	    
	    return render(
	        request,
	        'clown/author_detail.html',
	        context={'author':author_id,}
	    )


#HashTag View
class HashtagListView(generic.ListView):
    model = Hashtag
    context_object_name = 'hashtag_list'   # your own name for the list as a template variable
    template_name = 'clown/hashtag-list.html'  # Specify your own template name/location
    paginate_by = 10


    def get_queryset(self):
        return Hashtag.objects.all()[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HashtagListView, self).get_context_data(**kwargs)
        return context


class HashtagDetailView(generic.DetailView):
    model = Hashtag

    def hashtag_detail_view(request,pk):
	    try:
	        hashtag_id=Hashtag.objects.get(pk=pk)
	    except Hashtag.DoesNotExist:
	        raise Http404("Hashtag does not exist")

	    #book_id=get_object_or_404(Book, pk=pk)
	    
	    return render(
	        request,
	        'clown/hashtag_detail.html',
	        context={'hashtag':hashtag_id,}
	    )