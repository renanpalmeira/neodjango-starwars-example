from __future__ import unicode_literals

from django.test import TestCase

from app.nodes import Jedi, Planet

class NodeTestCase(TestCase):
	"""
	A long time ago in a galaxy far, far away....
	"""
	def test_node_all(self):
		result = Planet.objects.all()
		self.assertEqual(type(result), list)

	def test_node_filter(self):
		result = Jedi.objects.filter(name='Rey')
		self.assertEqual(len(result), 1)

	def test_node_filter_propery(self):
		result = Jedi.objects.filter(name='Rey')
		for item in result:
			self.assertEqual(type(item.name), unicode)
		self.assertEqual(len(result), 1)

	def test_node_get(self):
		result = Jedi.objects.get(name='Luke Skywalker')
		return True

	def test_node_get_all_relationships(self):
		result = Planet.objects.get(name='Kamino').relationships()
		terrain = result[0].terrain
		self.assertEqual(terrain, 'ocean')

	def test_node_relationship(self):
		result = Planet.objects.get(name='Kamino').Lived()
		return True

	def test_multi_node(self):
		rey = Jedi.objects.get(id=80)
		jakku = Planet.objects.get(name='Jakku')
		self.assertEqual(rey.name, 'Rey')
		self.assertEqual(jakku.terrain, 'deserts')