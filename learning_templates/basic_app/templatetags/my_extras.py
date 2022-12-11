from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    Deci functia scapa de toate valorile din string care sunt egale cu ce vine pe arg.
    """

    return value.replace(arg,'')

#register.filter('cut',cut) #aici trebuie sa inregistram filtrul creat. Primul argument e numele pe care
                          #vrem sa il aiba filtrul nostru. Al doilea argument e numele functiei care sta in spatele
                          #filtrului. In cazul nostru, acestea coincid.
