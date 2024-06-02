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

    for request in requests_list:
        selected_endpoint = load_balancer.route_request(request)
        load_balancer.log_request(request, selected_endpoint)
        try:
            response = requests.get(f'http://127.0.0.1:5000{selected_endpoint}')
            print(f'Request: {request}, Response: {response.json()}')
        except requests.exceptions.RequestException as e:
            print(f"Failed to reach endpoint {selected_endpoint}: {e}")

if __name__ == '__main__':
    simulate_requests()

