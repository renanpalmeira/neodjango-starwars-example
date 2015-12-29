from __future__ import unicode_literals

from django.test import TestCase

from app.nodes import Human

class ArticleTestCase(TestCase):
	def test_model(self):
		print Human.objects.all()