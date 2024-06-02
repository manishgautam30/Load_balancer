# src/load_balancer.py
import random
import logging
from src.mock_apis import api_endpoints
from src.queue_manager import QueueManager

class LoadBalancer:
    def __init__(self):
        self.endpoints = api_endpoints
        self.queue_manager = QueueManager()

    def route_request(self, request):
        # Example custom criteria routing logic
        if request['type'] == 'REST':
            return self.route_by_type('REST')
        elif request['payload_size'] > 1024:
            return self.route_by_payload_size(request['payload_size'])
        else:
            return self.random_route()

    def route_by_type(self, api_type):
        # Route based on API type
        return random.choice(self.endpoints[api_type])

    def route_by_payload_size(self, payload_size):
        # Route based on payload size
        return random.choice(self.endpoints['large_payload'])

    def random_route(self):
        # Randomized routing
        all_endpoints = [ep for endpoints in self.endpoints.values() for ep in endpoints]
        return random.choice(all_endpoints)

    def log_request(self, request, selected_endpoint):
        logging.info(f"Request: {request}, Routed to: {selected_endpoint}")

    def add_request_to_queue(self, request, queue_type='fifo', priority=0):
        if queue_type == 'fifo':
            self.queue_manager.add_request_fifo(request)
        elif queue_type == 'priority':
            self.queue_manager.add_request_priority(request, priority)
        elif queue_type == 'round_robin':
            self.queue_manager.add_request_round_robin(request)
        logging.info(f"Request added to {queue_type} queue: {request}")

    def get_request_from_queue(self, queue_type='fifo'):
        if queue_type == 'fifo':
            return self.queue_manager.get_request_fifo()
        elif queue_type == 'priority':
            return self.queue_manager.get_request_priority()
        elif queue_type == 'round_robin':
            return self.queue_manager.get_request_round_robin()
        return None

