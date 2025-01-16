from src import generate_request, process_request

def main():
    print("Система обробки заявок запущена.")
    try:
        while True:
            action = input("\nНатисніть [1] для додавання заявки, [2] для обробки заявки, [q] для виходу: ")
            if action == "1":
                generate_request()
            elif action == "2":
                process_request()
            elif action.lower() == "q":
                print("Програма завершена.")
                break
            else:
                print("[!] Невідома команда, спробуйте ще раз.")
    except KeyboardInterrupt:
        print("\nПрограма перервана користувачем.")

if __name__ == "__main__":
    main()