from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    replace a parameter in request.GET
    useful for paginated sites with filters for example

    :param dict context:
    :param kwargs:
    :rtype: str
    """
    d = context['request'].GET.copy()
    for k,v in kwargs.items():
        d[k] = v
    for k in [k for k,v in d.items() if not v]:
        del d[k]
    return d.urlencode()

@register.filter()
def param_remove(params, arg):
    """
    removes given arg from url parameters querydict

    :param QueryDict params:
    :param str arg:
    :rtype: str
    """
    d = params.copy()
    if arg in d:
        del d[arg]
    return d.urlencode()
