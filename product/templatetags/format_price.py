from django import template
from utils.numbers.format_price import format_price as fp

register = template.Library()


@register.filter
def format_price(value: str):
    return f'R$ {fp(value)}'
