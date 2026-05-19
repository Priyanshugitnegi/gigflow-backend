from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leads'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name