# Generated by Django 3.1.7 on 2021-05-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acccounts', '0004_auto_20210517_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]