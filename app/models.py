from __future__ import unicode_literals

from django.db import models

class Friend(models.Model):
	id_friend = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = "friend"