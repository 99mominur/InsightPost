from django.db import models
from .utils import slugfy_title
from froala_editor.fields import FroalaField
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = FroalaField()
    image = models.ImageField(upload_to="Images/blog_images")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from .utils import slugfy_title

            self.slug = slugfy_title(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
