import time
from generate_request import service_queue

# Функція для обробки заявок
def process_request():
    if not service_queue.empty():
        request_id = service_queue.get()
        print(f"[-] Обробка заявки: {request_id}")
        time.sleep(1)  # Імітація часу обробки
        print(f"[✓] Заявка {request_id} оброблена.")
    else:
        print("[!] Черга порожня. Заявки для обробки відсутні.")

