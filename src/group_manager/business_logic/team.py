from group_manager.models.custom_user import CustomUser


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
