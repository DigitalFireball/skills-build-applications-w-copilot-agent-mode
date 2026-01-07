from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workouts')


import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f'https://{codespace_name}-8000.app.github.dev/api' if codespace_name else '/api'
    return Response({
        'users': f'{base_url}/users/',
        'profiles': f'{base_url}/profiles/',
        'activities': f'{base_url}/activities/',
        'teams': f'{base_url}/teams/',
        'leaderboard': f'{base_url}/leaderboard/',
        'workouts': f'{base_url}/workouts/',
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
