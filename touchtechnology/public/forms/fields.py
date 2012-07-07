from django.forms import TypedChoiceField
from django.utils.translation import ugettext_lazy as _

from .widgets import BooleanSelect

POSITIVE = _(u'Yes')
NEGATIVE = _(u'No')


class BooleanChoiceField(TypedChoiceField):
    widget = BooleanSelect

    def __init__(self, positive=POSITIVE, negative=NEGATIVE, *args, **kwargs):
        choices = kwargs.pop('choices', ((1, positive), (0, negative)))
        super(BooleanChoiceField, self).__init__(choices=choices,
            coerce=lambda v: bool(int(v)), *args, **kwargs)
