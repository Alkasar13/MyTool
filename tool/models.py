from enum import IntEnum

from django.db import models
from django.utils import timezone
#from django.utils import timezone


class Choiseble(IntEnum):
    @classmethod
    def choises(cls):
        return [(x.value, x.name) for x in cls]


class Status(Choiseble):
    PROCESS = 0
    WINNER = 1
    LOOSER = 2

    def __str__(self):
        return str(self.value)


class Auction(models.Model):
    lot_id = models.CharField(max_length=20)
    cost_start = models.DecimalField(max_digits=16, decimal_places=2)
    cost_min = models.DecimalField(max_digits=16, decimal_places=2)
    cost_step = models.DecimalField(max_digits=16, decimal_places=2)
    cost_current = models.DecimalField(max_digits=16, decimal_places=2)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    win = models.PositiveIntegerField(
        choices=Status.choises(),
        default=Status.PROCESS)

    class Meta:
        ordering = ('published_date',)


def publish(self):
        self.published_date = timezone.now()
        self.save()
def delete(self):
    self.delete()