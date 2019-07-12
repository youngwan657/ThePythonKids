# Generated by Django 2.2.3 on 2019-07-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_date', models.DateTimeField()),
                ('answer', models.TextField(blank=True, default=None, null=True)),
                ('answer_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('right', models.IntegerField(default=0)),
                ('wrong_testcase', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
