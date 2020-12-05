from django.apps import AppConfig


class GroupManagerConfig(AppConfig):
    name = 'group_manager'

    def ready(self):
        import group_manager.signals.team
