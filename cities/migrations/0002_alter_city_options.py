# Generated by Django 4.2.1 on 2023-05-24 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('created',)},
        ),
    ]