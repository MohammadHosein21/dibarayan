import celery
from django.shortcuts import render
from .utils import send_config_to_client
from .tasks import process_received_data
from .models import Client


def send_config_and_run_docker(request, client_id):
    client = Client.objects.get(name=client_id)

    # Send config to the client and run mock container
    send_config_to_client(client.ip_address, 'mmdhosein', 'Hosein_77')

    app = celery.Celery('testProject', broker='memory://127.0.0.1:6379')

    # Get information about active tasks
    inspect_result = app.control.inspect('ca583517-899b-4aec-84e3-57d10f0a7ae5').report

    # Extract argsrepr information from the active tasks
    argsrepr_list = [task['argsrepr'] for tasks in inspect_result.values() for task in tasks] if inspect_result else []

    # Print the argsrepr information
    for argsrepr in argsrepr_list:
        # Asynchronously process the received data
        process_received_data(argsrepr).delay()

    return render(request, 'success.html', {'result': 'get tasks from mock client ans save in DB'})
