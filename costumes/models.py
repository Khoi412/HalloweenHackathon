from django.db import models
from django.contrib.auth.models import User

class Costume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='costumes')
    image = models.ImageField(upload_to='costume_images/')
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s costume at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'costume')

    def __str__(self):
        return f"{self.user.username} liked Costume {self.costume.id}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Costume {self.costume.id}"
