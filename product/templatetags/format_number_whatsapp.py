from django import template
from utils.numbers.format_number import format_phone_number

register = template.Library()


@register.filter
def format(value: str):
    return format_phone_number(value)
