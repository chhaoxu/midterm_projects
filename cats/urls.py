from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.MainView.as_view(), name='cats'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
    #path('', views.MainView.as_view(), name='breeds'),
    #path('main/create/', views.BreedCreate.as_view(), name='breed_create'),
    #path('main/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    #path('main/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
    #path('lookup/', views.MakeView.as_view(), name='make_list'),
    #path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    #path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    #path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
    ]
