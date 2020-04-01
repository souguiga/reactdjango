# Generated by Django 3.0.3 on 2020-03-23 16:28

import api.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('addess1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('items', api.fields.JSONField()),
                ('payment_intent', api.fields.JSONField()),
            ],
        ),
    ]