# Generated by Django 2.2.3 on 2019-07-11 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pub_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='choice_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='votes',
            new_name='vote',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='votes',
            new_name='vote',
        ),
    ]
