# Generated by Django 3.1.7 on 2021-04-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0004_auto_20210421_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creator',
            old_name='msg_id',
            new_name='id',
        ),
    ]
