import queue
import time

# Створити чергу заявок
requests_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request(request_id):
    request_data = f"Request #{request_id}"
    requests_queue.put(request_data)
    print(f"[GENERATED] {request_data}")

# Функція для обробки заявок
def process_request():
    if not requests_queue.empty():
        request_data = requests_queue.get()
        print(f"[PROCESSING] {request_data}")
        # Імітація обробки заявки
        time.sleep(1)
        print(f"[COMPLETED] {request_data}")
    else:
        print("[INFO] Queue is empty. No requests to process.")

# Головний цикл програми
def main():
    request_id = 1
    try:
        while True:
            action = input("Enter 'g' to generate a request, 'p' to process a request, or 'q' to quit: ").strip().lower()
            if action == 'g':
                generate_request(request_id)
                request_id += 1
            elif action == 'p':
                process_request()
            elif action == 'q':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("[ERROR] Invalid input. Please enter 'g', 'p', or 'q'.")
    except KeyboardInterrupt:
        print("\n[INFO] Program interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
