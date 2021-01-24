from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
#    ->      ROUTES ENDPOINTS, PASS IN VIEW, <NAME>
router.register('api/leads', LeadViewSet, 'leads')


#  THIS GIVES US ALL URLS REGISTERED FOR THE 'api/leads' ENDPOINT
urlpatterns = router.urls