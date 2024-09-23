from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>', views.MovieRetriveUpdateDestroyView.as_view(), name='movie_datail_update_delete'),
    path('movies/status', views.MovieStatusView.as_view(), name='movie_status')
]
