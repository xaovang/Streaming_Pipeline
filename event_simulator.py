import random
import time
from datetime import datetime

# Possible user actions
ACTIONS = ["click", "view", "purchase", "logout"]

def generate_event():
    event = {
        "user_id": random.randint(1, 1000),
        "action": random.choice(ACTIONS),
        "timestamp": datetime.now().isoformat()
    }
    return event

if __name__ == "__main__":
    while True:
        event = generate_event()
        print(event)
        time.sleep(1)  # Wait 1 second before the next event
