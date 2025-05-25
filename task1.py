from queue import Queue
from datetime import datetime

q = Queue()


def generate_request():
    time_now = datetime.now()  # current time
    timestamp_id = time_now.strftime("%Y%m%d%H%M%S%f")  # generate id based on timestamp
    timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")  # readable form for current time
    new_request = {"id": str(timestamp_id).replace(".", ""), "time": timestamp}

    q.put(new_request)
    print(f"New request with id: {new_request['id']}; created at {new_request['time']}")


def process_request():
    if not q.empty():
        request = q.get()
        print(f"Request {request['id']} by {request['time']} processed")
    else:
        print("No requests to process")


while True:
    generate_request()
    process_request()

    exit = input('To exit the program type "exit": ')
    if exit.lower() == "exit":
        break
