from django.db import models

from ..forms import BooleanChoiceField
from ..mixins import SouthTripleMixin


class BooleanField(SouthTripleMixin, models.BooleanField):
    """
    Custom `BooleanField` which overrides the formfield to use the much
    nicer `BooleanChoiceField` which presents two radio buttons rather
    than a checkbox.
    """
    def __init__(self, *args, **kwargs):
        # Custom `__init__` because the built-in BooleanField is expecting
        # a checkbox input where "unticked" == False and "ticked" == True.
        if 'default' not in kwargs and not kwargs.get('null'):
            kwargs['default'] = False
        models.Field.__init__(self, *args, **kwargs)

    def formfield(self, form_class=BooleanChoiceField, **kwargs):
        return super(BooleanField, self).formfield(
            form_class=form_class, **kwargs)
