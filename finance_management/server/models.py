from datetime import date

from django.db import models

from server.constants import CategoryType


class TimeStampedModel(models.Model):
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if kwargs and kwargs.get('update_fields'):
            if 'udate' not in kwargs['update_fields']:
                kwargs['update_fields'].append("udate")
        super(TimeStampedModel, self).save(*args, **kwargs)

    def update_safely(self, refresh=True, **kwargs):
        fields = []
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])
            fields.append(kwarg)
        self.save(update_fields=fields)
        if refresh:
            self.refresh_from_db()

    class Meta(object):
        abstract = True

    def __str__(self):
        return "{}".format(self.id)


class Category(TimeStampedModel):
    id = models.AutoField(db_column='category_id', primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(choices=CategoryType.CHOICES, max_length=255)
    group = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Source(TimeStampedModel):
    id = models.AutoField(db_column="source_id", primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Transaction(TimeStampedModel):
    id = models.AutoField(db_column='transaction_id', primary_key=True)
    transaction_date = models.DateField(default=date.today)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category_id')
    source = models.ForeignKey(Source, models.DO_NOTHING, db_column="source_id")
    amount = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)
