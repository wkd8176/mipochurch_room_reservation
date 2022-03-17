from django import template

register = template.Library()

@register.filter
def datetimeForFC(value):
    time = value.strftime("%Y-%m-%dT%H:%M:%S")

    return time