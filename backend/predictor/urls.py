
from django.urls import path

from .views import (
    home,
    PredictDiseaseView,
    DashboardView,
    PredictionHistoryView
)

urlpatterns = [

    path("", home),

    path(
        "predict/",
        PredictDiseaseView.as_view()
    ),

    path(
        "dashboard/",
        DashboardView.as_view()
    ),

    path(
        "history/",
        PredictionHistoryView.as_view()
    ),
]

