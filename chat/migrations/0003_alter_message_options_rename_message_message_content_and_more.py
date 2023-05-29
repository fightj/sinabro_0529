# Generated by Django 4.2.1 on 2023-05-29 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_board_pw'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_room_users_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date_added',)},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.AddField(
            model_name='room',
            name='pw',
            field=models.CharField(default=1234, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_board',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_room', to='board.board'),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.room'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
