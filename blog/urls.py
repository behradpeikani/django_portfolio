from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post/', views.PostList.as_view(), name='post_list'),
    path('category/<int:pk>/', views.BlogCategoryList.as_view(), name='blog_category_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
