from collections import deque

def is_palindrome(input_string):
    # Попереднє очищення рядка: видалення пробілів і приведення до нижнього регістру
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Додавання символів до двосторонньої черги
    char_deque = deque(cleaned_string)
    
    # Перевірка символів з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не співпадають, це не паліндром
    
    return True  # Якщо всі символи співпадають, це паліндром

# Введення рядка користувачем
user_input = input("Введіть рядок для перевірки на паліндром: ")

# Перевірка та виведення результату
if is_palindrome(user_input):
    print(f"Рядок '{user_input}' є паліндромом.")
else:
    print(f"Рядок '{user_input}' не є паліндромом.")