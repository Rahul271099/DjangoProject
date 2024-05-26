from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView, UserProjectsListView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('user/projects/', UserProjectsListView.as_view(), name='user-projects'),
]
