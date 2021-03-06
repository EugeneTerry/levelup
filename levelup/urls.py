"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
# from levelupapi.models.eventstatus import EventStatus
from levelupapi.models.games import Games
from levelupapi.views import (
    EventView,
    GameTypeView,
    GameView,
    register_user,
    login_user,
    get_gamer_profile,
    # EventStatusView 
    )

from django.conf.urls import include
from django.urls import path

# from levelupapi.views.eventstatus import EventStatusView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
# router.register(r'statuses', EventStatusView, 'status')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('profile', get_gamer_profile),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('levelupreports.urls')),
]