# Generated by Django 4.0.4 on 2022-05-28 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_pictures'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['-post_date']},
        ),
    ]
