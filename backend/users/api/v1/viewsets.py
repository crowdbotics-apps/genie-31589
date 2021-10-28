from rest_framework import authentication
from users.models import GigAccount
from .serializers import GigAccountSerializer
from rest_framework import viewsets


class GigAccountViewSet(viewsets.ModelViewSet):
    serializer_class = GigAccountSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = GigAccount.objects.all()
