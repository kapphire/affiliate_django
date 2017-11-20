# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_affiliate',
        ),
        migrations.AddField(
            model_name='post',
            name='image_forex',
            field=models.ImageField(blank=True, upload_to='forex'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_gambling',
            field=models.ImageField(blank=True, upload_to='gambling'),
        ),
    ]
