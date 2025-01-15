from django import template

register = template.Library()


@register.filter
def get_val(dictionary, key):
    """Returns the value of a dictionary for the given key."""
    try:
        return dictionary.get(key, None)
    except AttributeError:
        return None
