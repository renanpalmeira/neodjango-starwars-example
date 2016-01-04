from __future__ import absolute_import, unicode_literals

from django.dispatch import receiver
from neodjango.db.models.signals import pre_node_init

from .nodes import Jedi

@receiver(pre_node_init, sender=Jedi)
def initial_jedi(sender, **kwargs):
	pass
