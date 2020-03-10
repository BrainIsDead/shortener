from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views import View

from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets, views, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Link
from .serializers import LinkSerializer, LinkListSerializer

from secrets import token_urlsafe


class LinkViewset(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    method_serializer_classes = {
        ('GET'): LinkListSerializer,
        ('POST'): LinkSerializer
    }

    queryset = Link.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        filters.OrderingFilter,
    )
    ordering_fields = ['count',]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            full_url = request.data['full_url']
            short_url = settings.HOST_NAME + token_urlsafe(4) + '/'
            user = self.request.user
            link = Link(
                full_url=full_url,
                short_url=short_url,
                user = user
            )
            link.save()
            return Response(
                data={'short_url': short_url},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        link = Link.objects.get(pk=kwargs['pk'])
        link.is_active = False
        link.save()
        return Response(status=status.HTTP_200_OK)

    def get_serializer_class(self):
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls


class FollowLinkView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        short_url = settings.HOST_NAME + kwargs['short_url'] + '/'
        link = get_object_or_404(Link, short_url=short_url, is_active=True)
        link.count += 1
        link.save()
        return Response(
            headers={"Location": link.full_url},
            status=status.HTTP_301_MOVED_PERMANENTLY
        )
