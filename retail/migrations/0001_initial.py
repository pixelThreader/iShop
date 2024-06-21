# Generated by Django 4.2.9 on 2024-06-20 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cupons",
            fields=[
                ("cupon_sno", models.AutoField(primary_key=True, serialize=False)),
                ("cupon_id", models.CharField(max_length=20)),
                ("cupon_name", models.CharField(max_length=50)),
                ("cupon_discount", models.IntegerField()),
                ("cupon_alloted_day", models.DateField(auto_now=True)),
                ("cupon_expiry_day", models.DateField(null=True)),
                ("cupon_code", models.CharField(max_length=10)),
                (
                    "cupon_used_status",
                    models.CharField(
                        choices=[("used", "used"), ("unused", "unused")],
                        default="unused",
                        max_length=50,
                    ),
                ),
                (
                    "cupon_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "cupons",
            },
        ),
        migrations.CreateModel(
            name="Info_Payment_for_one",
            fields=[
                ("order_sno", models.AutoField(primary_key=True, serialize=False)),
                ("user_is_orderd", models.BooleanField(null=True)),
                ("user_order_id", models.CharField(max_length=10, null=True)),
                ("user_order_Code", models.CharField(max_length=13)),
                ("user_order_nameFirst", models.CharField(max_length=50)),
                ("user_order_nameLast", models.CharField(max_length=50)),
                ("user_order_email", models.CharField(max_length=150)),
                ("user_order_address1", models.CharField(max_length=500)),
                (
                    "user_order_address2_opt",
                    models.CharField(max_length=500, null=True),
                ),
                ("user_order_country", models.CharField(max_length=50)),
                ("user_order_state", models.CharField(max_length=50)),
                ("user_order_pin", models.CharField(max_length=6)),
                ("user_order_phone1", models.CharField(max_length=13)),
                ("user_order_phone2_opt", models.CharField(max_length=13, null=True)),
                ("user_order_cupon_applied", models.BooleanField()),
                ("user_order_product_qty", models.IntegerField()),
                ("user_order_product_size", models.CharField(max_length=50)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_order_cupon",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retail.cupons",
                    ),
                ),
                (
                    "user_order_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.allproducts",
                    ),
                ),
            ],
            options={
                "verbose_name": "Info_Payment_for_one",
                "verbose_name_plural": "Info_Payment_for_one",
            },
        ),
    ]