from django import template

register = template.Library()

@register.filter
def times(number):
    """ترجع نطاق (range) من 0 إلى الرقم المحدد"""
    return range(number)
