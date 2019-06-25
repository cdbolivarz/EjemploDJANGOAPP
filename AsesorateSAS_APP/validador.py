from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_entero(horas):
    if (horas>0 and int(horas)==horas):
        raise ValidationError(
        _('%(horas)s debe ser un número entero mayor a cero.'),
        params={'horas': horas},
    )