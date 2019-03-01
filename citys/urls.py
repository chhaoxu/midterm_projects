from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.MainView.as_view(), name='citys'),
    path('main/create/', views.CityCreate.as_view(), name='city_create'),
    path('main/<int:pk>/update/', views.CityUpdate.as_view(), name='city_update'),
    path('main/<int:pk>/delete/', views.CityDelete.as_view(), name='city_delete'),
    path('lookup/', views.StateView.as_view(), name='state_list'),
    path('lookup/create/', views.StateCreate.as_view(), name='state_create'),
    path('lookup/<int:pk>/update/', views.StateUpdate.as_view(), name='state_update'),
    path('lookup/<int:pk>/delete/', views.StateDelete.as_view(), name='state_delete'),
    #path('', views.MainView.as_view(), name='b:wqreeds'),
    #path('main/create/', views.BreedCreate.as_view(), name='breed_create'),
    #path('main/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    #path('main/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
    #path('lookup/', views.MakeView.as_view(), name='make_list'),
    #path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    #path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    #path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
    ]

