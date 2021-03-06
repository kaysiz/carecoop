# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChairRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'CHAIRPERSONS',
                'verbose_name_plural': 'CHAIRPERSONS',
            },
        ),
        migrations.CreateModel(
            name='LoansCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position')),
                ('organization', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organization')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images%Y/%m/%d', verbose_name='Image')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'MEMBER',
                'verbose_name_plural': 'MEMBERS',
            },
        ),
        migrations.CreateModel(
            name='SupervisoryCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position on Board')),
                ('nationality', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nationality')),
                ('image', models.ImageField(upload_to='images%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'SUPERVISORY COMMITTEE',
                'verbose_name_plural': 'SUPERVISORY COMMITTEES',
            },
        ),
        migrations.AddField(
            model_name='chairremarks',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Members'),
        ),
    ]
