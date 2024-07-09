from django.utils.text import slugify
import random
import string

# random text generator


def random_text(max_length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=max_length))


def slugfy_title(text):
    text = slugify(text)
    from .models import BlogPost

    if BlogPost.objects.filter(slug=text).exists():
        text = slugfy_title(text + random_text(5))
    return text
