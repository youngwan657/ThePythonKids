# Generated by Django 2.2.3 on 2019-07-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_quiz_answer_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='list.Quiz'),
            preserve_default=False,
        ),
    ]
