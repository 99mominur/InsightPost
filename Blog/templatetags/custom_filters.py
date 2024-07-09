from django import template

register = template.Library()


@register.filter(name="truncate_words")
def truncate_words(value, arg):
    return " ".join(value.split()[: int(arg)])
