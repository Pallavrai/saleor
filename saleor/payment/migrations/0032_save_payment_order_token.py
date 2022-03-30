# Generated by Django 3.2.12 on 2022-02-24 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0127_add_order_number_and_alter_order_token"),
        ("payment", "0031_merge_0030_auto_20210908_1346_0030_payment_partial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="order_token",
            field=models.UUIDField(null=True),
        ),
        migrations.RunSQL(
            """
            UPDATE payment_payment
            SET order_token = (
                SELECT token
                FROM order_order
                WHERE payment_payment.order_id = order_order.id
            )
            WHERE order_id IS NOT NULL;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AlterField(
            model_name="payment",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="payments",
                to="order.order",
                to_field="number",
            ),
        ),
    ]