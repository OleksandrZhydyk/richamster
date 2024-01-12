from django.db import models


class SomeModel(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "SomeModels"
