from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Profile, Activity, Team
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        Profile.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating superhero users and teams...')
        marvel = ['Iron Man', 'Captain America', 'Thor', 'Black Widow']
        dc = ['Superman', 'Batman', 'Wonder Woman', 'Flash']
        marvel_team, _ = Team.objects.get_or_create(name='Marvel')
        dc_team, _ = Team.objects.get_or_create(name='DC')
        all_profiles = []
        for hero in marvel:
            user = User.objects.create_user(username=hero.lower().replace(' ', ''), email=f'{hero.lower().replace(" ", "")}@marvel.com')
            profile = Profile.objects.create(user=user, bio=f'{hero} is a Marvel superhero')
            marvel_team.members.add(profile)
            all_profiles.append(profile)
        for hero in dc:
            user = User.objects.create_user(username=hero.lower().replace(' ', ''), email=f'{hero.lower().replace(" ", "")}@dc.com')
            profile = Profile.objects.create(user=user, bio=f'{hero} is a DC superhero')
            dc_team.members.add(profile)
            all_profiles.append(profile)
        # Add activities
        for profile in all_profiles:
            Activity.objects.create(profile=profile, activity_type='training', duration_minutes=60, distance_km=10.0)
        self.stdout.write('Creating leaderboard and workouts collections in MongoDB...')
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index('email', unique=True)
        db.leaderboard.insert_many([
            {'team': 'Marvel', 'points': 100},
            {'team': 'DC', 'points': 90}
        ])
        db.workouts.insert_many([
            {'name': 'Super Strength', 'description': 'Strength training for superheroes'},
            {'name': 'Speed Run', 'description': 'Speed training for speedsters'}
        ])
        self.stdout.write(self.style.SUCCESS('octofit_db populated with superhero test data'))
