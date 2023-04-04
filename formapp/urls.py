from rest_framework import routers
from .api import FormSimViewSet


router = routers.DefaultRouter()

router.register('api/formsim',FormSimViewSet,'formsim' )

urlpatterns = router.urls



