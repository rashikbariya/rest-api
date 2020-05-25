from django.urls import path
from status.views import StatusDetailAPIView, StatusListAPIView

urlpatterns = [
    path('', StatusListAPIView.as_view()), #/api/status/ -> list/create
    path('<id>/', StatusDetailAPIView.as_view()), #/api/status/<int>/ ->detail/update/delete
]
