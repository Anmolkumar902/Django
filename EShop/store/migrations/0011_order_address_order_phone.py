# Generated by Django 4.1.7 on 2023-04-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
