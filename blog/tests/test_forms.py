from django.test import TestCase
from blog.forms import CommentForm

class TestCommentForm(TestCase):
	def test_valid_data(self):
		form = CommentForm(data={"author": "behrad", "body": "nice"})
		self.assertTrue(form.is_valid())

	def test_invalid_data(self):
		form = CommentForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEqual(len(form.errors), 2)