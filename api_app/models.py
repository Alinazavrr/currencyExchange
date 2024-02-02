from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    currency_base = models.ForeignKey(Currency, on_delete=models.CASCADE)
    currency_final = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_final')
    time_last_update = models.DateTimeField()
    time_next_update = models.DateTimeField()
    rate = models.FloatField()

    def __str__(self):
        return f'{self.currency_base} - {self.date} - {self.rate}'

    class Meta:
        ordering = ['-time_next_update']