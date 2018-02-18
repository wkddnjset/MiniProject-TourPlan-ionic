from django.db import models

# Create your models here.
class ProductList(models.Model):
    img_url     = models.ImageField(blank=True)
    title       = models.CharField(max_length=100)
    sub_title   = models.TextField()

    def __str__(self):
        return str(self.title)