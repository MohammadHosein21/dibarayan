from celery import shared_task
from django.utils import timezone
from .models import DataModel
import json


@shared_task
def process_received_data(message):
    try:
        # Extract the data from the message
        data = json.loads(message)

        # Process and save data to the database
        DataModel.objects.create(
            stream_id=data['stream_id'],
            timestamp=data['timestamp'],
            status=data['status'],
            log=data['log'],
            session_id=data['session_id']
        )

    except Exception as e:
        print(f"Error processing data: {e}")
