from django.db import models
from django.urls import reverse


class Board(models.Model):
    name = models.CharField(help_text="Board name")

    def get_absolute_url(self):
        """Returns the URL to access a particular instance."""
        return reverse("board-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the object."""
        return self.name


class Category(models.Model):
    name = models.CharField(help_text="Category name")
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the object."""
        return self.name


class Attribute(models.Model):
    description = models.TextField(help_text="Attribute description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the object."""
        return self.description
