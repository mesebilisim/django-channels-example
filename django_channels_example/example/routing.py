from django.conf.urls import url
from django.urls import path

from example import consumers

websocket_urlpatterns = [
    path('ws/', consumers.TestConsumer),
]