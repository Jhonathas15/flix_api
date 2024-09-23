from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>', views.ActorRetriveUpdateDestroyView.as_view(), name='actor_datail_update_delete'),
]
