from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile instance when a new User is created.

    Args:
        sender: The model class that triggered the signal.
        instance: The instance of the model being saved.
        created: Boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the UserProfile whenever the User instance is saved.
    """
    instance.profile.save()
