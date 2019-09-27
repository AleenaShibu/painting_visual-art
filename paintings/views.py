from django.shortcuts import render

from django.views.generic import ListView,DetailView 
from django.views.generic.edit import DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Painting
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin

class PaintingListView(ListView):
	model = Painting
	template_name ='home.html'

class PaintingDetailView( LoginRequiredMixin,PermissionRequiredMixin,DetailView):
	model = Painting
	template_name ='detail.html'
	login_url = 'login'
	permission_required = 'paintings.special_access' 

class AddPaintingView(CreateView):
	model = Painting
	template_name ='addpainting.html'
	fields = ['name','artist_name','subject','origin','medium','image']

class DeletePaintingView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Painting
	template_name = 'delete.html'
	success_url = reverse_lazy('home')
	login_url = 'login'

	


class SearchPaintingView(ListView):
	model = Painting
	template_name = 'searchview.html'

	def ger_Queryset(self):
		query =self.request.GET['q']
		return Painting.objects.filter(name__icontains=query)
	
