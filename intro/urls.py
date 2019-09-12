from django.urls import path
from . import views

app_name = 'intro'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('register/', views.UserFormView.as_view(), name='register'),

    path('person/add/', views.PersonCreate.as_view(), name='person-add'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person-update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person-delete'),
]
