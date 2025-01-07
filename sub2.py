# Subscriber
from kuksa_client.grpc import VSSClient
from datetime import datetime

with VSSClient('127.0.0.1', 55555) as client:
    for updates in client.subscribe_current_values([
        'Vehicle.Speed',
        'Vehicle.CurrentLocation.Timestamp',
    ]):
        # Extract speed and timestamp
        speed = updates['Vehicle.Speed'].value
        sent_timestamp = updates['Vehicle.CurrentLocation.Timestamp'].value
        
        # Calculate the delay
        received_time = datetime.utcnow()
        sent_time = datetime.fromisoformat(sent_timestamp)
        delay = (received_time - sent_time).total_seconds()
        
        print(f"Received updated speed: {speed}, sent at {sent_timestamp}, delay: {delay} seconds")
