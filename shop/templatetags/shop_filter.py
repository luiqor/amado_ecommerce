from django import template

register = template.Library()


@register.filter
def to_range(value):
    return range(value)


@register.filter
def subtract_from_five(value):
    return 5 - value
