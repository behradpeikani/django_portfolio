from django.test import SimpleTestCase
from django.urls import resolve, reverse
from portfolio.views import ProjectList, ProjectDetail

class TestUrls(SimpleTestCase):
    def test_project_list(self):
        url = reverse('portfolio:project_list')
        self.assertEqual(resolve(url).func.view_class, ProjectList)

    def test_project_detail(self):
        url = reverse('portfolio:project_detail', args=[1,])
        self.assertEqual(resolve(url).func.view_class, ProjectDetail)