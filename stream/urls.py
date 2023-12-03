from django.urls import path, include
from .views import send_config_and_run_docker

urlpatterns = [
    path('<client_id>/', send_config_and_run_docker),
]