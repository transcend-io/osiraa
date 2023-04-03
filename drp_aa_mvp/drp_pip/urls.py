from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),

    path('.well-known/data-rights.json', views.static_discovery, name='discovery'),
    path('v1/data-rights-request/', views.validate_pynacl, name='receive_request'),
    path('v1/data-rights-request/<str:request_id>', views.request_handler, name='request_handler'),
    path('v1/agent/<str:aa_id>', views.agent, name='agent_router_ugghhh'),
]
