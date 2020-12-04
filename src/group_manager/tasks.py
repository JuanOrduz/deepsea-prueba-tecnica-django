from celery import shared_task
from celery.decorators import task

from group_manager.models.team import Team
from group_manager.business_logic import team as team_logic


@shared_task
def notify_new_team(team_id):
    print("Notifying new team")
    team = Team.objects.get(id=team_id)
    team_logic.notify_creation_to_admins(team)


@task(name='check_teams_size')
def check_teams_size():
    print("Checking teams size")
    team_logic.check_max_size_teams()
