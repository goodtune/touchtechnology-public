from django.forms import RadioSelect


class BooleanSelect(RadioSelect):
    def render(self, name, value, attrs=None, choices=()):
        value = int(value or 0)
        return super(BooleanSelect, self).render(name, value, attrs, choices)
