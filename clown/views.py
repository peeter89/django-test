from django.shortcuts import render
from .models import Author, Hashtag

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