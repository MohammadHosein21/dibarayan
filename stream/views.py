from django.shortcuts import render
from .utils import send_config_to_client
from .utils import run_docker_container
from .tasks import process_received_data
from .models import Client
import redis

def send_config_and_run_docker(request, client_id):
    client = Client.objects.get(name=client_id)

    # Replace these values with your actual configuration
    config = "sender_config:\nserver_ip: 192.168.1.4\nport: 6379\nsend_rate: 10\ncelery_task_name: process_received_data"

    # Send configuration to the client
    send_config_to_client(client.ip_address, 'mmdhosein', 'Hosein_77', config)

    # Run Docker container on the client
    # result = run_docker_container(client.ip_address, 'mmdhosein', 'Hosein_77')
    result = 0
    # Mocked data for testing

    # Asynchronously process the received data
    process_received_data.delay()

    return render(request, 'success.html', {'result': result})

