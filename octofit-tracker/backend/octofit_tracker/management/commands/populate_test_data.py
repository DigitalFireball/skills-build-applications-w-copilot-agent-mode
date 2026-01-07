from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Profile, Activity, Team


class Command(BaseCommand):
    help = 'Populate octofit_db with sample test data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample users and data...')
        users = []
        for i in range(1, 4):
            username = f'user{i}'
            user, created = User.objects.get_or_create(username=username, defaults={'email': f'{username}@example.com'})
            if created:
                user.set_password('test')
                user.save()
            users.append(user)

        profiles = []
        for u in users:
            profile, _ = Profile.objects.get_or_create(user=u, defaults={'bio': f'Bio for {u.username}'})
            profiles.append(profile)

        # Create teams
        team1, _ = Team.objects.get_or_create(name='Alpha')
        team2, _ = Team.objects.get_or_create(name='Beta')
        team1.members.set(profiles[:2])
        team2.members.set(profiles[1:])

        # Create activities
        Activity.objects.get_or_create(profile=profiles[0], activity_type='run', duration_minutes=30, distance_km=5.0)
        Activity.objects.get_or_create(profile=profiles[1], activity_type='cycle', duration_minutes=45, distance_km=20.0)
        Activity.objects.get_or_create(profile=profiles[2], activity_type='walk', duration_minutes=60, distance_km=6.0)

        self.stdout.write(self.style.SUCCESS('Sample data created'))
