from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ThoughtEntry(models.Model):
    title = models.CharField(max_length=200, help_text="或许有总结")
    date = models.DateField(help_text="写下文字的时刻")
    content = models.TextField(help_text="有什么想说的就写下来吧")
    author = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="thought_entries",
        help_text="留名于此，空白则为匿名"
    )
    is_public = models.BooleanField(default=False, help_text="要不要公开呢？")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "日志条目"
        verbose_name_plural = "日志条目列表"

    def __str__(self):
        return f"{self.title} ({self.date})"

class MessageEntry(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sent_messages",
        help_text="留名于此"
    )
    content = models.TextField(help_text="留言内容")
    is_public = models.BooleanField(default=False, help_text="要不要公开呢？")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "留言"
        verbose_name_plural = "留言列表"

    def __str__(self):
        return f"Message from {self.sender} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"