from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('created',)