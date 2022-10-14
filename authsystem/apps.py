from django.apps import AppConfig

class AuthsystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authsystem'

    def ready(self) -> None:
        import authsystem.signals
