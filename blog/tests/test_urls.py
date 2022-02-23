from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import BlogCategoryList, PostList, PostDetail

class TestUrls(SimpleTestCase):
    def test_post_list(self):
        url = reverse('blog:post_list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail(self):
        url = reverse('blog:post_detail', args=[1,])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_post_list(self):
        url = reverse('blog:blog_category_list', args=[1,])
        self.assertEqual(resolve(url).func.view_class, BlogCategoryList)