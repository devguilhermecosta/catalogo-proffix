from django import template

register = template.Library()


@register.filter
def format(value: str):
    return value.replace(
        '(', ''
        ).replace(')', '').replace('-', '').replace(' ', '').strip()
