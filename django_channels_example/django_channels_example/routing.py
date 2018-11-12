from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import example.routing


application = ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(
        URLRouter(
            example.routing.websocket_urlpatterns,
        ),
    ),
})
