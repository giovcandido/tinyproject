from django.db import models


class TinyMessage(models.Model):
    content = models.TextField(
        max_length=300,
        help_text='Enter a tiny message'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
