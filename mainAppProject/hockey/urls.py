from hockey import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.AbstractUserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'joueurs', views.PlayerViewSet)
router.register(r'equipes', views.TeamViewSet)
router.register(r'horaires', views.TimetableViewSet)
router.register(r'entitesMorales', views.AbstractMoralEntityViewSet)
router.register(r'matches', views.MatchViewSet)
router.register(r'resultatsMatches', views.MatchResultViewSet)
router.register(r'partenaires', views.PartnerSerializerViewSet)