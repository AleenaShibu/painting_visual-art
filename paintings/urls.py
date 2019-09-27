from django.urls import path
from .views import PaintingListView,PaintingDetailView,AddPaintingView,DeletePaintingView,SearchPaintingView

urlpatterns = [
    path('',PaintingListView.as_view(),name ='home'),
    path('detail/<int:pk>/',PaintingDetailView.as_view(),name = 'detail'),
    path('addpainting/',AddPaintingView.as_view(),name = 'addpainting'),
    path('delete/<int:pk>/',DeletePaintingView.as_view(),name = 'delete'),
    path('search/',SearchPaintingView.as_view(),name ='search'),
    ]




