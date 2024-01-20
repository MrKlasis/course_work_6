from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag
def date_time(format_string):
    dt = datetime.strptime(format_string, '%Y-%m-%d %H:%M:%S')
    return dt.strftime('%Y-%m-%d %H:%M:%S')
