from hockey import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'abstract_users', views.AbstractUserViewSet)
router.register(r'abstract_groups', views.GroupViewSet)
#router.register(r'joueurs', views.JoueurViewSet)