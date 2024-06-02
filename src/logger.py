# src/logger.py
import logging

logging.basicConfig(filename='load_balancer.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')
