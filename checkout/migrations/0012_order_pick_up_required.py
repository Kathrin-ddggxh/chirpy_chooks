# Generated by Django 3.2 on 2023-03-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pick_up_required',
            field=models.BooleanField(default=False),
        ),
    ]