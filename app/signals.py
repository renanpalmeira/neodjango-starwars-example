from __future__ import absolute_import, unicode_literals

from django.dispatch import receiver
from neodjango.db.models.signals import pre_node_init

from .nodes import Jedi
from .tasks import add

@receiver(pre_node_init, sender=Jedi)
def initial_jedi(sender, **kwargs):
	add.delay(1, 2)
