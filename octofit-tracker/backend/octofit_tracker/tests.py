from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Activity, Team, Leaderboard, Workout



    def test_create_profile_and_activity(self):
        user = User.objects.create_user(username='tester', password='pass')
        profile = Profile.objects.create(user=user, bio='hello')
        self.assertEqual(Profile.objects.count(), 1)
        activity = Activity.objects.create(profile=profile, activity_type='run', duration_minutes=30, distance_km=5.0)
        self.assertEqual(Activity.objects.count(), 1)
        team = Team.objects.create(name='Team A')
        team.members.add(profile)
        self.assertEqual(team.members.count(), 1)

    def test_leaderboard_and_workout(self):
        Leaderboard.objects.create(team='Marvel', points=100)
        Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(Workout.objects.count(), 1)
