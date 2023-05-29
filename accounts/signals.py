from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from chat.models import Room
from django.utils.text import slugify
@receiver(post_save, sender=User)
def create_chat_user_room(sender, instance, created, **kwargs):
    if created:
        # 생성된 유저에 대한 채팅방 생성 로직
        username = str(instance.username)
        slug = slugify(username)

        existing_slugs = Room.objects.filter(slug__startswith=slug)
        if existing_slugs:
            max_number = max([int(s.slug[len(slug):]) for s in existing_slugs if s.slug[len(slug):].isdigit()])
            slug = f"{slug}{max_number + 1}"

        room = Room.objects.create(name=f"{instance.username}'s Room", slug=slug)
        room.users.add(instance)