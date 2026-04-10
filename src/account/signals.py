from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def store_old_avatar(sender, instance, **kwargs):

    old_user = sender.objects.filter(id=instance.id).only("avatar").first()

    instance._old_avatar = old_user.avatar if old_user else None


@receiver(post_save, sender=User)
def delete_old_avatar(sender, instance, **kwargs):
    old_avatar = getattr(instance, "_old_avatar", None)
    new_avatar = instance.avatar

    if old_avatar and old_avatar != new_avatar:
        old_avatar.storage.delete(old_avatar.name)
