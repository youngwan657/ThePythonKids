# Generated by Django 2.2.3 on 2019-07-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20190711_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='wrong_testcase',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
