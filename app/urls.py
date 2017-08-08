from django.conf.urls import include, url
from rest_framework import routers
from views import OwnerAPIView, DogAPIView, CatAPIView


router = routers.DefaultRouter()
router.register(r'owner', OwnerAPIView)
router.register(r'dog', DogAPIView)
router.register(r'cat', CatAPIView)

urlpatterns = [
    url('^', include(router.urls))
]
