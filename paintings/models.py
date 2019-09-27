from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Painting(models.Model):

	class Meta:
		permissions =[
            ("special_access", "Can read all paintings")]
	name = models.CharField(max_length=50)
	artist_name =models.CharField(max_length=50)
	subject =models.TextField()
	origin =models.CharField(max_length=50)
	medium =models.CharField(max_length=50)
	image = models.ImageField(upload_to='image/', blank =True)

	def __str__(self):
		return self.movie_name[ :50]
		
	def get_absolute_url(self):
		return reverse('subject', args=[str(self.id)])	






