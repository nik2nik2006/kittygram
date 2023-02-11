from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
# path('', hello),
#   path('cats/<int:pk>', CatViewSet.as_view()),
#   path('cats/', CatViewSet.as_view()),
