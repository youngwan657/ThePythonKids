# Generated by Django 2.2.3 on 2019-07-18 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_remove_answer_case'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='expected_result',
            new_name='expected_answer',
        ),
    ]
