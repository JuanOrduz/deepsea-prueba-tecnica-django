from django.dispatch import receiver
from django.db.models.signals import post_save

from group_manager.models.team import Team
from group_manager.business_logic import team as team_logic


@receiver(post_save, sender=Team)
def handle_content_completed(sender, instance, created, **kwargs):
    if created:
        team_logic.notify_creation_to_admins(instance)
