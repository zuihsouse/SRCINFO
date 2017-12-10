# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SRCCompany', '0003_auto_20171209_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plug_name', models.CharField(max_length=30, verbose_name='组件名称')),
                ('plug_version', models.CharField(max_length=30, verbose_name='组件版本')),
                ('plug_starttime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('plug_updatetime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('plug_subdomain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plug_in_subdomain', to='SRCCompany.Subdomain')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='server_os',
            field=models.GenericIPAddressField(null=True, verbose_name='操作系统'),
        ),
        migrations.AddField(
            model_name='server',
            name='server_subdomain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server_in_subdomain', to='SRCCompany.Subdomain'),
        ),
    ]