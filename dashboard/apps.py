from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    Configuration class for the Dashboard app.

    This class sets the app's name and ensures that custom signal handlers
    in the `dashboard.signals` module are imported and ready when the app
    is initialized.

    Methods:
        ready: Imports signal handlers to connect them with the appropriate
        models or events during app initialization.
    """
    name = 'dashboard'

    def ready(self):
        import dashboard.signals
