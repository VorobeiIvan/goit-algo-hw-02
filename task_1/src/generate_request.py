from queue import Queue
import random 

# Create the queue
service_queue = Queue()

# Function to generate new requests
def generate_request():
    """Function for generating new requests"""
    request_id = f"Request-{random.randint(1000, 9999)}"  # Generate a unique request ID
    service_queue.put(request_id)  # Add the request to the queue
    print(f"[+] New request added to the queue: {request_id}")
