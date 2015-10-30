# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('html_grade', models.IntegerField(max_length=10, choices=[(b'0', 0), (b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5), (b'6', 6), (b'7', 7), (b'8', 8), (b'9', 9), (b'10', 10)])),
                ('css_grade', models.IntegerField(max_length=10)),
                ('javascript_grade', models.IntegerField(max_length=10)),
                ('python_grade', models.IntegerField(max_length=10)),
                ('django_grade', models.IntegerField(max_length=10)),
                ('ios_grade', models.IntegerField(max_length=10)),
                ('android_grade', models.IntegerField(max_length=10)),
            ],
        ),
    ]
