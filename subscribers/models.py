from django.db import models

# Create your models here.
class Subscriber(models.Model):
    """A subscriber model."""

    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')

    def __str__(self):
        """String representation of this object."""
        return self.full_name