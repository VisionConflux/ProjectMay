# Generated by Django 5.0 on 2024-01-01 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_topic_room_host_message_room_topic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='core.room'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic', to='core.topic'),
        ),
    ]
