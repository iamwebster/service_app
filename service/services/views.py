from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Subsctiption
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subsctiption.objects.all()
    serializer_class = SubscriptionSerializer

