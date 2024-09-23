from django.urls import path
from . import views


urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='genre_create_list'),
    path('genres/', views.GenreCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>', views.GenereRetriveUpdateDestroyView.as_view(), name='genre_datail_update_delete'),
]
