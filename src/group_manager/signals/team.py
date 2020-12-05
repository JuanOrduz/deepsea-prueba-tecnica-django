from django.dispatch import receiver
from django.db.models.signals import post_save

from group_manager.models.team import Team
from group_manager.tasks import notify_new_team


@receiver(post_save, sender=Team)
def handle_team_creation(sender, instance, created, **kwargs):
    if created:
        notify_new_team.delay(instance.id)
