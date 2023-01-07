from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'

    # Define ready() function to use signals
    def ready(self):
        import app.accounts.signals
