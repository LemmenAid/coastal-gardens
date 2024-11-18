from django.db import models


class Contact(models.Model):
    """
    This model stores information about users who reach out, including their
    name, email, gardening experience level, garden zone, message, and whether
    the request has been read.
    """
    EXPERIENCE_CHOICES = [
        ('novice', "I'm new to gardening"),
        ('intermediate', "I have some experience"),
        ('advanced', "I'm an experienced gardener"),
        ('expert', "I'm a professional or expert gardener"),
    ]

    ZONE_CHOICES = [
        ('8a', '8a'),
        ('8b', '8b'),
        ('9a', '9a'),
        ('9b', '9b'),
        ('10a', '10a'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    gardening_experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default='novice',
        verbose_name="What's your level of gardening experience?"
    )
    garden_zone = models.CharField(
        max_length=3,
        choices=ZONE_CHOICES,
        verbose_name="Which garden zone do you live in?",
        null=True,
        blank=True
    )
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"
