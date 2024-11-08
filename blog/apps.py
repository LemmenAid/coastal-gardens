from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' application.

    Attributes:
    - `default_auto_field`: Sets the type of primary key to use for models in this app to BigAutoField.
    - `name`: Specifies the app's name, which is 'blog'.

    This class is used to configure app-specific settings for the 'blog' app, which Django uses for app registry.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
