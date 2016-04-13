from __future__ import unicode_literals

from neodjango.db import models

class Planet(models.Node):

	name = models.StringProperty()

	class Meta:
		display = "name"

class Jedi(models.Node):
	class Meta:
		label = "Human"
		display = "name"