from django import template

register = template.Library()

try:
    from cdecimal import Decimal
except ImportError:
    from decimal import Decimal

def __validate_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)


def __manage_float_decimal(value, arg):
    if isinstance(value, float) and isinstance(arg, Decimal):
        value = Decimal(str(value))
    if isinstance(value, Decimal) and isinstance(arg, float):
        arg = Decimal(str(arg))
    return value, arg

@register.filter(name='abs')
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


@register.filter
def sub(value, arg):
    """
    substract arg from value

    :param int/float/Decimal value:
    :param int/float/Decimal arg:
    :return:
    """
    try:
        v, a = __manage_float_decimal(__validate_numeric(value), __validate_numeric(arg))
        return v - a
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''


sub.is_safe = False


@register.filter
def add(value, arg):
    """
    add arg to value

    :param int/float/Decimal value:
    :param int/float/Decimal arg:
    :return:
    """
    try:
        v, a = __manage_float_decimal(__validate_numeric(value), __validate_numeric(arg))
        return v + a
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''


add.is_safe = False

@register.filter
def mul(value, arg):
    """
    multiply arg  with value

    :param int/float/Decimal value:
    :param int/float/Decimal arg:
    :return:
    """
    try:
        v, a = __manage_float_decimal(__validate_numeric(value), __validate_numeric(arg))
        return v * a
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''

mul.is_safe = False\

@register.filter
def div(value, arg):
    """
    divide value with arg

    :param int/float/Decimal value:
    :param int/float/Decimal arg:
    :return:
    """
    try:
        v, a = __manage_float_decimal(__validate_numeric(value), __validate_numeric(arg))
        return v / a
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''

div.is_safe = False