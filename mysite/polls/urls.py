from django.urls import path

from . import views
app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="polls-index"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('owner', views.owner, name='owner'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]