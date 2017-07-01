from django.utils.text import slugify


def to_slug(string):
    return slugify(string)
