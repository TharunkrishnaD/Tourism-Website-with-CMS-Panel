# Generated by Django 4.2.7 on 2024-03-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CcustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('destination', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ccustomer_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagesname', models.CharField(max_length=255)),
                ('description', models.JSONField()),
            ],
            options={
                'db_table': 'pages_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField()),
            ],
            options={
                'db_table': 'user_reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_table',
                'managed': False,
            },
        ),
    ]