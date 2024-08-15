# Generated by Django 5.1 on 2024-08-15 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('test_app', '0001_initial'), ('test_app', '0002_userdetail'), ('test_app', '0003_anothermodel')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
                'indexes': [models.Index(fields=['email'], name='user_email_7bbb4c_idx')],
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_app.user')),
            ],
            options={
                'db_table': 'user_detail',
                'indexes': [models.Index(fields=['user'], name='user_detail_user_id_45022b_idx')],
            },
        ),
        migrations.CreateModel(
            name='AnotherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'another_model',
                'indexes': [models.Index(fields=['email'], name='another_mod_email_bf132c_idx')],
            },
        ),
    ]
