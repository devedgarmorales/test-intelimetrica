from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, estadisticas_restaurantes

router = DefaultRouter()
router.register(r'restaurantes', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurantes/estadisticas', estadisticas_restaurantes, name='estadisticas_restaurantes'),
]