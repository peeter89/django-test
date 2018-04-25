from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

# class State(models.Model):
# 	name = models.CharField(max_length=20, help_text="Enter state name (e.g. publish, unpublish...)")

# 	def __str__(self):
# 		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_create = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ["last_name","first_name"]

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)
     
class Hashtag(models.Model):
	name = models.CharField(max_length=50, unique=True, help_text="Hashtag name")
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	date_create = models.DateField(auto_now_add=True)
	
	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

# class Post(models.Model):
# 	name = models.CharField(max_length=50)
# 	description = models.CharField(max_length=250, null=True, blank=True)
# 	image = models.CharField(max_length=250)
# 	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
# 	state = models.ForeignKey('State', on_delete=models.PROTECT)
# 	hashtag = models.ManyToManyField(Hashtag,help_text='Select a Hashtag for Post')
# 	date_create = models.DateField(auto_now_add=True)
# 	date_update = models.DateField(auto_now=True)

# 	def display_hashtag(self):
        
# 		return ', '.join([ hashtag.name for hashtag in self.hashtag.all()[:10] ])
# 	display_hashtag.short_description = 'Hashtag'

# 	class Meta:
# 		ordering = ["date_create"]

# 	def get_absolute_url(self):
# 		return reverse('post-detail', args=[str(self.id)])

# 	def __str__(self):
# 		return self.name