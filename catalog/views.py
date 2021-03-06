from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RenewBookForm


# Create your views here.

def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_books=Book.objects.all().count()
	num_books_filter=Book.objects.filter(title__startswith='Level').count()
	num_instances=BookInstance.objects.all().count()
	# Available books (status = 'a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()  # The 'all()' is implied by default.
	num_genres = Genre.objects.count()

	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1

	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_books':num_books, 'num_books_filter': num_books_filter ,'num_instances':num_instances,
		'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_genres': num_genres, 
		'num_visits':num_visits},
	)




@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
    

#Book

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 2


    def get_queryset(self):
        return Book.objects.all()[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request,pk):
	    try:
	        book_id=Book.objects.get(pk=pk)
	    except Book.DoesNotExist:
	        raise Http404("Book does not exist")

	    #book_id=get_object_or_404(Book, pk=pk)
	    
	    return render(
	        request,
	        'catalog/book_detail.html',
	        context={'book':book_id,}
	    )

#Author

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'   # your own name for the list as a template variable
    template_name = 'catalog/author_list.html'  # Specify your own template name/location
    paginate_by = 10


    def get_queryset(self):
        return Author.objects.all()[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def book_detail_view(request,pk):
	    try:
	        author_id=Author.objects.get(pk=pk)
	    except Author.DoesNotExist:
	        raise Http404("Author does not exist")

	    #book_id=get_object_or_404(Book, pk=pk)
	    
	    return render(
	        request,
	        'catalog/author_detail.html',
	        context={'author':author_id,}
	    )


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllUserListView(PermissionRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_all_user.html'
    paginate_by = 10
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'05/01/2018',}
    


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


#@login_required
#def my_view(request):
    

#class MyView(PermissionRequiredMixin, View):
    #permission_required = 'catalog.can_mark_returned'
     #Or multiple permissions
    #permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    # Note that 'catalog.can_edit' is just an example
    # the catalog application doesn't have such permission!