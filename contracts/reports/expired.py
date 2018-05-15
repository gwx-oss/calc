from django.utils import timezone

from contracts.models import Contract
from .base import BaseMetric


class Metric(BaseMetric):
    '''
    Find labor rates whose contracts are expired.
    '''

    def count(self) -> int:
        return Contract.objects.filter(
            contract_end__lt=timezone.now()
        ).count()

    desc = 'labor rates are from expired contracts.'