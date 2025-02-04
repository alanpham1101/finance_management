# This is an empty retroload file created by a custom Django command

from __future__ import unicode_literals

from django.db import migrations

from server.models import Category, Source
from server.constants import CategoryType, CategoryGroup


def init_category_data():
    category_data = [
        Category(name='Market', type=CategoryType.EXPENSE, group=CategoryGroup.LIVING_EXPENSE),
        Category(name='Eating', type=CategoryType.EXPENSE, group=CategoryGroup.LIVING_EXPENSE),
        Category(name='Moving', type=CategoryType.EXPENSE, group=CategoryGroup.LIVING_EXPENSE),
        Category(name='Shopping', type=CategoryType.EXPENSE, group=CategoryGroup.INCIDENTAL_EXPENSE),
        Category(name='Entertainment', type=CategoryType.EXPENSE, group=CategoryGroup.INCIDENTAL_EXPENSE),
        Category(name='Beauty', type=CategoryType.EXPENSE, group=CategoryGroup.INCIDENTAL_EXPENSE),
        Category(name='Health', type=CategoryType.EXPENSE, group=CategoryGroup.INCIDENTAL_EXPENSE),
        Category(name='Charity', type=CategoryType.EXPENSE, group=CategoryGroup.INCIDENTAL_EXPENSE),
        Category(name='Bill', type=CategoryType.EXPENSE, group=CategoryGroup.FIXED_EXPENSE),
        Category(name='House', type=CategoryType.EXPENSE, group=CategoryGroup.FIXED_EXPENSE),
        Category(name='Family', type=CategoryType.EXPENSE, group=CategoryGroup.FIXED_EXPENSE),
        Category(name='Investment', type=CategoryType.EXPENSE, group=CategoryGroup.INVESTMENT_SAVING),
        Category(name='Studying', type=CategoryType.EXPENSE, group=CategoryGroup.INVESTMENT_SAVING),
        Category(name='Debt Collection', type=CategoryType.INCOME),
        Category(name='Business', type=CategoryType.INCOME),
        Category(name='Profit', type=CategoryType.INCOME),
        Category(name='Bonus', type=CategoryType.INCOME),
        Category(name='Subsidy', type=CategoryType.INCOME),
        Category(name='Salary', type=CategoryType.INCOME),
    ]
    Category.objects.bulk_create(category_data)


def init_source_data():
    source_data = [
        Source(name='Cash'),
        Source(name='E-wallet'),
        Source(name='Bank')
    ]
    Source.objects.bulk_create(source_data)


def create_init_data():
    init_category_data()
    init_source_data()


class Migration(migrations.Migration):
    create_init_data()
