from __future__ import unicode_literals

from neodjango.db import models

class Human(models.Node):
	class Meta:
		label = "Human"