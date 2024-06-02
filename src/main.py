# src/main.py
import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.load_balancer import LoadBalancer
from src.logger import logging
import requests

def simulate_requests():
    load_balancer = LoadBalancer()

    # Example requests
    requests_list = [
        {'type': 'REST', 'payload_size': 512},
        {'type': 'REST', 'payload_size': 2048},
        {'type': 'gRPC', 'payload_size': 1024}
    ]

    # Add requests to queues
    for request in requests_list:
        load_balancer.add_request_to_queue(request, queue_type='fifo')
        load_balancer.add_request_to_queue(request, queue_type='priority', priority=request['payload_size'])
        load_balancer.add_request_to_queue(request, queue_type='round_robin')

    # Process requests from queues
    for queue_type in ['fifo', 'priority', 'round_robin']:
        print(f"\nProcessing {queue_type} queue:")
        while True:
            request = load_balancer.get_request_from_queue(queue_type)
            if request is None:
                break
            selected_endpoint = load_balancer.route_request(request)
            load_balancer.log_request(request, selected_endpoint)
            try:
                response = requests.get(f'http://127.0.0.1:5000{selected_endpoint}')
                print(f'Request: {request}, Response: {response.json()}')
            except requests.exceptions.RequestException as e:
                print(f"Failed to reach endpoint {selected_endpoint}: {e}")

if __name__ == '__main__':
    simulate_requests()

