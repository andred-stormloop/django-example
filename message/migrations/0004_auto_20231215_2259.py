# Generated by Django 3.2.23 on 2023-12-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_message_upvotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='comments',
            field=models.ManyToManyField(related_name='message_comments', to='message.Comment'),
        ),
    ]
