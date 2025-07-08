import random
import time
import threading
import queue
import csv
from datetime import datetime

# Actions you want to simulate
ACTIONS = ["click", "view", "purchase", "logout"]
event_queue = queue.Queue()

def generate_event():
    return {
        "user_id": random.randint(1, 1000),
        "action": random.choice(ACTIONS),
        "timestamp": datetime.now().isoformat()
    }

def producer():
    while True:
        event = generate_event()
        print(f"[Producer] Generated: {event}")
        event_queue.put(event)
        time.sleep(1)

def consumer():
    action_counts = {}

    # Open the CSV file once in append mode
    with open('event_counts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write header if file is empty
        file.seek(0, 2)  # Move to end
        if file.tell() == 0:
            writer.writerow(['timestamp', 'click', 'view', 'purchase', 'logout'])

        while True:
            event = event_queue.get()
            action = event["action"]

            # Update the count for this action
            action_counts[action] = action_counts.get(action, 0) + 1

            # Print what we're processing
            print(f"[Consumer] Processing: {event}")
            print(f"[Stats] {action_counts}")

            # Get current timestamp
            timestamp = datetime.now().isoformat()

            # Write the current counts to CSV
            writer.writerow([
                timestamp,
                action_counts.get('click', 0),
                action_counts.get('view', 0),
                action_counts.get('purchase', 0),
                action_counts.get('logout', 0)
            ])
            file.flush()  # Make sure it's written to disk

            event_queue.task_done()

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
