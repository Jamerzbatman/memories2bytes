import hashlib
import time
from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    user = models.ForeignKey(User, related_name='media_details', on_delete=models.CASCADE)
    hash = models.CharField(max_length=64, unique=True, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Field to store the total quote amount

    def save(self, *args, **kwargs):
        # Generate a unique hash based on user ID and current timestamp
        unique_string = f"{self.user.id}{time.time()}"
        self.hash = hashlib.sha256(unique_string.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hash}"
    

class MediaDetail(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('image', 'Image'),
    ]
    quote = models.ForeignKey(Quote, related_name='media_details', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    condition = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.quantity} - {self.condition}"
