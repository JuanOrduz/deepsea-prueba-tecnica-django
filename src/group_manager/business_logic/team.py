from group_manager.models.custom_user import CustomUser
from group_manager.models.team import Team
from django.core.mail import EmailMessage


def assign_users(team, users_ids):
    users = []
    for user_id in users_ids:
        try:
            user = CustomUser.objects.get(id=user_id)
            users.append(user)
        except:
            pass
    team.users.set(users)
    team.save()
    return team


def update_users(team, users_ids):
    team.users.through.objects.all().delete()
    users = []
    for user_id in users_ids:
        try:
            user = CustomUser.objects.get(id=user_id)
            users.append(user)
        except:
            pass
    team.users.set(users)
    team.save()
    return team


def notify_creation_to_admins(team):
    admins = CustomUser.objects.filter(is_superuser=True)
    for admin in admins:
        email = EmailMessage(
            'New Team created',
            'New Team called ' + team.name + ' was created.',
            to=[admin.email],
        )
        try:
            email.send()
        except:
            pass


def check_max_size_teams(max_size=10):
    teams = Team.objects.all()
    admins = CustomUser.objects.filter(is_superuser=True)

    for team in teams:
        if len(team.users.all()) > max_size:
            for admin in admins:
                email = EmailMessage(
                    'Team ' + team.name + ' is overpopulated',
                    'Team ' + team.name + ' has more than 10 users',
                    to=[admin.email],
                )
                try:
                    email.send()
                except:
                    pass
