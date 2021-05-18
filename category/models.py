from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    category_name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.category_name
