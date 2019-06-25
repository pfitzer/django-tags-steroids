import calendar
from django import template
from django.utils.translation import ugettext_lazy as _

try:
    from cdecimal import Decimal
except ImportError:
    from decimal import Decimal

register = template.Library()

def __validate_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)

@register.filter()
def day_name(day):
    """get the localized name for a day.

    :param int day: index of day, monday==0
    :raise: AssertionError
    :rtype: str
    """
    assert type(day) is int, "Wrong parameter, expected int!"
    return _(calendar.day_name[day])

@register.filter()
def day_abbr(day):
    """get the localized abbrevation for a day. starts mondays with 0

    :param int day: index of day, monday==0
    :raise: AssertionError
    :rtype: str
    """
    assert type(day) is int, "Wrong parameter, expected int!"
    return _(calendar.day_abbr[day])

@register.filter()
def month_name(month):
    """get the localized name for a month.

    :param int month: index of day, monday==0
    :raise: AssertionError
    :rtype: str
    """
    assert type(month) is int, "Wrong parameter, expected int!"
    return _(calendar.month_name[month])

register.filter(name='abs')
def absolute(value):
    """return the absolute value

    :param int/float/Decimal value:
    """
    try:
        return abs(__validate_numeric(value))
    except (ValueError, TypeError):
        try:
            return abs(value)
        except Exception:
            return ''
absolute.is_safe = False
