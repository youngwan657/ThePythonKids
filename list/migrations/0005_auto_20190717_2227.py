# Generated by Django 2.2.3 on 2019-07-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20190717_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='expected_result',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='testcase',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
