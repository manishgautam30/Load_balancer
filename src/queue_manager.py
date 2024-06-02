# src/queue_manager.py
import queue
import logging

class QueueManager:
    def __init__(self):
        self.fifo_queue = queue.Queue()
        self.priority_queue = queue.PriorityQueue()
        self.round_robin_queues = [queue.Queue() for _ in range(3)]
        self.current_rr_index = 0

    def add_request_fifo(self, request):
        self.fifo_queue.put(request)
        logging.info(f"Request added to FIFO queue: {request}")

    def get_request_fifo(self):
        if not self.fifo_queue.empty():
            return self.fifo_queue.get()
        return None

    def add_request_priority(self, request, priority):
        self.priority_queue.put((priority, request))
        logging.info(f"Request added to Priority queue: {request}, Priority: {priority}")

    def get_request_priority(self):
        if not self.priority_queue.empty():
            return self.priority_queue.get()[1]
        return None

    def add_request_round_robin(self, request):
        self.round_robin_queues[self.current_rr_index].put(request)
        logging.info(f"Request added to Round Robin queue {self.current_rr_index}: {request}")
        self.current_rr_index = (self.current_rr_index + 1) % len(self.round_robin_queues)

    def get_request_round_robin(self):
        for i in range(len(self.round_robin_queues)):
            queue_index = (self.current_rr_index + i) % len(self.round_robin_queues)
            if not self.round_robin_queues[queue_index].empty():
                return self.round_robin_queues[queue_index].get()
        return None

