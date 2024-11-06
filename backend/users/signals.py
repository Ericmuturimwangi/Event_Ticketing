from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ticket

@receiver(post_save, sender=Ticket)
def send_ticket_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'New Ticket Created: {instance.title}'
        message = f'Your ticket has been created with the following details:\n\n{instance.description}'
        recipient_list = [instance.user.email]
    else:
        subject = f'Ticket Updated: {instance.title}'
        message = f'Your ticket has been updated. New status: {instance.status}\n\nDetails: {instance.description}'
        recipient_list = [instance.user.email]

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )