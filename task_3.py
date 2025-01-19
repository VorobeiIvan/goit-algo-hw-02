def check_balance(expression):
    stack = []
    # Словник для відповідності відкриваючих та закриваючих дужок
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in "({[":  # Якщо це відкрита дужка
            stack.append(char)
        elif char in ")}]":  # Якщо це закрита дужка
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Відкриваюча дужка для поточної закритої знайдена, знімаємо її зі стеку
            else:
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

# Введення рядка користувачем
user_input = input("Введіть рядок з дужками для перевірки: ")

# Перевірка та виведення результату
result = check_balance(user_input)
print(result)
