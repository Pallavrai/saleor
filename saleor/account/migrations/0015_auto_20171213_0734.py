# Generated by Django 1.11.5 on 2017-12-13 13:34
from __future__ import unicode_literals

from django.db import migrations

import saleor.account.models


class Migration(migrations.Migration):
    dependencies = [("account", "0014_auto_20171129_1004")]

    replaces = [("userprofile", "0015_auto_20171213_0734")]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="phone",
            field=saleor.account.models.PossiblePhoneNumberField(
                blank=True, default="", max_length=128, verbose_name="phone number"
            ),
        )
    ]
