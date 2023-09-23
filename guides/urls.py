from django.urls import path

from .views import GuideListCreateView, GuideRetrieveUpdateDeleteView

urlpatterns = [
    path("guides/", GuideListCreateView.as_view(), name="guide-list-create"),
    path(
        "guides/<int:pk>/", GuideRetrieveUpdateDeleteView.as_view(), name="guide-detail"
    ),
]
