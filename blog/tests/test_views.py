from django.test import TestCase, Client
from django.urls import reverse
# from blog.models import Category, Post, Comment

class TestView(TestCase):
	def setUp(self):
		self.client = Client()

	def test_user_post_list_GET(self):
		response = self.client.get(reverse('blog:post_list'))  
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/blog_list.html')

	# def test_user_blog_category_list_GET(self):
	# 	# response = self.client.get(reverse('blog:blog_category_list', args=[1,]))
	# 	response = self.client.get('/blog/category/1/')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'blog/blog_category.html')