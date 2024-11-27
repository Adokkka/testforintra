# Generated by Django 5.1.3 on 2024-11-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('namefull', models.CharField(max_length=255)),
                ('rem', models.TextField(blank=True, null=True)),
                ('uid', models.UUIDField()),
            ],
        ),
    ]
