import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class MentorSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mentor = models.ForeignKey(Mentor, related_name="client_sessions", on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name="mentor_sessions", on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    session_length = models.IntegerField(blank=True, null=True)  # seconds
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.mentor.user.username


class MentorSessionEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mentor_session = models.ForeignKey(MentorSession, related_name="events", on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    session_length = models.IntegerField(blank=True, null=True)  # seconds

    def __str__(self):
        return str(self.id)

