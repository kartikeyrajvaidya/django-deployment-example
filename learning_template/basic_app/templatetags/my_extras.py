from django import template

register = template.Library()

@register.filter(name='cutthatshit')
def cut(value,arg):

    return value.replace(arg,'')

register.filter('cutthatshit',cut)
