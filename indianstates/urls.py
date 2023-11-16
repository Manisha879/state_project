# indianstates/urls.py

from django.urls import path
from .views import IndianStateListView, IndianStateDetailView, IndianStateCreateView, IndianStateUpdateView, IndianStateDeleteView
from indianstates import views
urlpatterns = [
    path('', IndianStateListView.as_view(), name='indianstate_list'),
    path('<int:pk>/', IndianStateDetailView.as_view(), name='indianstate_detail'),
    path('add/', IndianStateCreateView.as_view(), name='indianstate_add'),
    path('<int:pk>/edit/', IndianStateUpdateView.as_view(), name='indianstate_edit'),
    path('<int:pk>/delete/', IndianStateDeleteView.as_view(), name='indianstate_delete'),
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
]
