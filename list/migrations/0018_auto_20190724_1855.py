# Generated by Django 2.2.3 on 2019-07-25 01:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0017_quiz_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='explanation',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
