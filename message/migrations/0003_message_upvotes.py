# Generated by Django 3.2.23 on 2023-12-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
