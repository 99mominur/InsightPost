from django.utils.text import slugify
import random
import string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six 

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()


def random_text(max_length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=max_length))


def slugfy_title(text):
    text = slugify(text)
    from .models import BlogPost

    if BlogPost.objects.filter(slug=text).exists():
        text = slugfy_title(text + random_text(5))
    return text
