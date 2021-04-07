from django.urls import include, path
from rest_framework.routers import Route, SimpleRouter

from .views import PositionViewSet, ShipViewSet


class CustomReadOnlyRouter(SimpleRouter):
    """
    A custom router to handle our API
    """

    routes = [
        Route(
            url=r"^{prefix}/$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        Route(
            url=r"^{prefix}/{lookup}/$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=True,
            initkwargs={"suffix": "List"},
        ),
    ]


router = CustomReadOnlyRouter()
router.register(r"ships", ShipViewSet, basename="ships")
router.register(r"positions", PositionViewSet, basename="positions")

urlpatterns = [
    path("", include(router.urls)),
]
