from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, calories=300, date='2026-01-04')
        self.workout = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        self.leaderboard = Leaderboard.objects.create(team=marvel, points=750)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().name, 'Spider-Man')

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Activity.objects.first().type, 'Running')

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Workout.objects.first().name, 'Hero HIIT')

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(Leaderboard.objects.first().points, 750)
