# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-08 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharPrimaryKeyModel',
            fields=[
                ('chr', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DirectPrimaryKeyModel',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False, verbose_name=b'Number')),
            ],
        ),
        migrations.CreateModel(
            name='SalmonellaTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rawid_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rawid_fk', to=settings.AUTH_USER_MODEL)),
                ('rawid_fk_direct_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rawid_fk_direct_pk', to='project_example.DirectPrimaryKeyModel')),
                ('rawid_fk_limited', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rawid_fk_limited', to=settings.AUTH_USER_MODEL)),
                ('rawid_many', models.ManyToManyField(blank=True, null=True, related_name='rawid_many', to=settings.AUTH_USER_MODEL)),
                ('salmonella_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salmonella_fk', to=settings.AUTH_USER_MODEL)),
                ('salmonella_fk_char_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salmonella_fk_char_pk', to='project_example.CharPrimaryKeyModel')),
                ('salmonella_fk_direct_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salmonella_fk_direct_pk', to='project_example.DirectPrimaryKeyModel')),
                ('salmonella_fk_limited', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salmonella_fk_limited', to=settings.AUTH_USER_MODEL)),
                ('salmonella_many', models.ManyToManyField(blank=True, null=True, related_name='salmonella_many', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
