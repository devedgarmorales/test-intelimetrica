from rest_framework import viewsets
from .models import Restaurante
from .serializers import RestaurantSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.db.models import Avg, StdDev


# Create your views here.

def estadisticas_restaurantes(request):
    latitud = float(request.GET.get('latitud'))
    longitud = float(request.GET.get('longitud'))
    radio = float(request.GET.get('radio'))

    if not all([latitud, longitud, radio]):
        return JsonResponse({'error': 'Se deben proporcionar latitud, longitud y radio'}, status=400)

    try:
        latitud = float(latitud)
        longitud = float(longitud)
        radio = float(radio)
    except ValueError:
        return JsonResponse({'error': 'Latitud, longitud y radio deben ser números válidos'}, status=400)

    punto_central = Point(longitud, latitud, srid=4326)

    restaurantes_en_radio = Restaurante.objects.filter(
        ubicacion__distance_lte=(punto_central, D(m=radio))
    )

    count = restaurantes_en_radio.count()
    avg_rating = restaurantes_en_radio.aggregate(avg_rating=Avg('clasificacion'))['avg_rating'] or 0
    std_dev_rating = restaurantes_en_radio.aggregate(std_dev_rating=StdDev('clasificacion'))['std_dev_rating'] or 0

    response_data = {
        'count': count,
        'avg': avg_rating,
        'std': std_dev_rating
    }

    return JsonResponse(response_data)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestaurantSerializer

    def list(self, request, *args, **kwargs):
        latitud = request.GET.get('latitud')
        longitud = request.GET.get('longitud')
        radio = request.GET.get('radio')
        if latitud and longitud and radio:
            return estadisticas_restaurantes(request)

        return super().list(request, *args, **kwargs)
