
from django.contrib import admin
from django.urls import path, include
# from updates.views import (
#     json_example, 
#     JsonCBV, 
#     JsonCBV2, 
#     SerializedDetailView, 
#     SerializedListView
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', include('status.urls'))


    # path('json-example/', json_example),
    # path('json-ex/', JsonCBV.as_view()),
    # path('json-ex2/', JsonCBV2.as_view()),
    # path('json-serial-detail/', SerializedDetailView.as_view()),
    # path('json-serial-list/', SerializedListView.as_view()),
]
