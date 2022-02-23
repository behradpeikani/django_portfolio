from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project

class TestView(TestCase):
	def setUp(self):
		self.client = Client()

	def test_user_project_list_GET(self):
		response = self.client.get(reverse('portfolio:project_list'))  
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'portfolio/project_list.html')

	# def test_user_project_detail_GET(self):
	# 	response = self.client.get(reverse('portfolio:project_detail'), args=[1,])  
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'portfolio/project_detail.html')