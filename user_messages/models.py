from django.db import models
import uuid
# Create your models here.


class Message(models.Model):

    user_choices = (
        ('A', 'User A'),
        ('B', 'User B'),
        ('Z', 'Bot')
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.CharField(choices=user_choices,
                            default='A', null=False, blank=False, max_length=255)
    text = models.TextField(null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'ID: {self.id}'

    def save(self, *args, **kwargs):
        # Call the real save() method
        super(Message, self).save(*args, **kwargs)
