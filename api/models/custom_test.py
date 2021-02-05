from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.base_model import BaseModel


class CustomTest(BaseModel):
    class Type(models.TextChoices):
        MLPA = "MLPA", _('MLPA')
        SEQ = "SEQ", _('SEQ')
        NGS = "NGS", _('NGS')

    class Finding(models.TextChoices):
        POSITIVE = "POSITIVE", _('Positive')
        NEGATIVE = "NEGATIVE", _('Negative')
        INCONCLUSIVE = "INCONCLUSIVE", _('Inconclusive')

    class Meta:
        db_table = 'custom_test'

    name = models.CharField(max_length=255)

    type = models.CharField(max_length=255, choices=Type.choices, default=Type.MLPA.value)
    finding = models.CharField(max_length=255, choices=Finding.choices, default=Finding.POSITIVE.value)

    methodology = models.TextField(blank=True)
    limitations = models.TextField(blank=True)
    references = models.TextField(blank=True)
