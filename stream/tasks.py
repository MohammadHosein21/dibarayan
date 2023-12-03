import celery
from celery import shared_task
from django.utils import timezone
from .models import DataModel
import json


@shared_task
def process_received_data(message):
    try:
        # Extract the data from the message
        data = json.loads(message['argsrepr'])
        print(data)
        # Process and save data to the database
        DataModel.objects.create(
            stream_id=data['stream_id'],
            timestamp=timezone.now(),
            status=data['status'],
            log_type=data['log']['type'],
            coordinates=data['log']['coordinates'],
            thumbnail=data['log']['thumbnail'],
            session_id=data['session_id']
        )

        # You can add any additional processing logic here

    except Exception as e:
        # Handle exceptions appropriately (e.g., log the error)
        print(f"Error processing data: {e}")
