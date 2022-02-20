from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='project_list'),
    path('detail/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
]
