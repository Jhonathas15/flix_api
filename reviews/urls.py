from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>', views.ReviewRetriveUpdateDestroyView.as_view(), name='review_datail_update_delete'),
]
