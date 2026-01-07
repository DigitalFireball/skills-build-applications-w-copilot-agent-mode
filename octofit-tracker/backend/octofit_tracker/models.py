from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile({self.user.username})"


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Profile, related_name='teams', blank=True)

    def __str__(self):
        return self.name



class Activity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.profile.user.username}"


# MongoDB-only collections (no migrations, for direct access)
class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'workouts'
