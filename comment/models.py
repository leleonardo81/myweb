from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.username, self.snipped_message())
    
    def snipped_message(self):
        if len(self.comment) > 20 :
            return self.comment[:20] + " ..."
        return self.comment
    
class Reply(models.Model):
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    reply_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, related_name="replies")
    def __str__(self):
        return self.reply_message

class Like(models.Model):
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)