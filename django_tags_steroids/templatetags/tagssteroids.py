import calendar
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.filter()
def day_name(day):
    """get the localized name for a day.

    :param day: index of day, monday==0
    :type day: int
    :rtype: str
    """
    assert type(day) is int, "Wrong parameter, expected int!"
    return _(calendar.day_name[day])

@register.filter()
def day_abbr(day):
    """get the localized abbrevation for a day. starts mondays with 0

    :param day: index of day, monday==0
    :type day: int
    :rtype: str
    """
    assert type(day) is int, "Wrong parameter, expected int!"
    return _(calendar.day_abbr[day])

@register.filter()
def month_name(month):
    """get the localized name for a month.

    :param month: index of day, monday==0
    :type month: int
    :rtype: str
    """
    assert type(month) is int, "Wrong parameter, expected int!"
    return _(calendar.month_name[month])
