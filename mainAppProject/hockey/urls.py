from hockey import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.AbstractUserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'timetables', views.TimetableViewSet)
router.register(r'moralEntities', views.AbstractMoralEntityViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'matches', views.MatchViewSet)
router.register(r'matchResults', views.MatchResultViewSet)
router.register(r'partnerships', views.PartnerSerializerViewSet)