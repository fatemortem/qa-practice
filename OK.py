from datetime import datetime
def log_result(status, action, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp} {status}] {action} - {message}\n")
def check_age():
    age = input("Введите возраст: ")
    if not age.isdigit():
        print("Возраст должен быть числом.")
        log_result("ERROR", "Проверка возраста", "введено не число)")
    elif int(age) < 18:
        print("Вам должно быть больше 18 лет.")
        log_result("ERROR", "Проверка возраста", "возраст < 18")
    else:
        print("Возраст принят.")
        log_result("OK", "Проверка возраста", "Возраст принят")

def check_email():
    email = input("Введите email").strip()
    if email == "":
        print("Email не может быть пустым.")
        log_result("ERROR", "Проверка на пустое поле", "пустой email")
    elif  "@" not in email or "." not in email:
        print("Неверный формат Email.")
        log_result("ERROR", "Проверка формата email", "отсутствуют '@' и(или) '.'")
    else:
        at_index = email.index("@")
        dot_index = email.rindex(".")
        if at_index == 0:
            print("Email не может начинаться с '@'")
            log_result("ERROR", "проверка на первый символ", "@ в самом начале")
        elif at_index > dot_index:
            print("'@' должна быть до '.'")
            log_result("ERROR", "проверка первоочередности '@'", ". была до @")
        else:
            print("Email принят.")
            log_result("OK", "проверка email", "Email принят")

def count_vowels():
    text = input("Введите текст: ").lower()
    vowels = "аеёиоуыэюя"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"Количество гласных букв: {count}")
    log_result("OK", "Подсчет гласных", f"'{text}' - {count} гласных")
    if text.strip() == "":
        print("Строка не может быть пустой")
        log_result("ERROR", "Подсчет гласных", "пустая строка")
        return

def check_login_password():
    login = input("Введите ваш логин: ").strip()
    if login == "":
        print("Логин не может быть пустым.")
    elif len(login) < 3:
        print("Логин слишком короткий (меньше 3 символов).")
    elif len(login) > 15:
        print("Логин слишком длинный (больше 15 символов).")
    else:
        print("Логин принят.")

        password = input("Создайте пароль: ")
        if len(password) < 6:
            print("Пароль слишком короткий (меньше 6 символов).")
        elif not any(char.isdigit() for char in password):
            print("Пароль должен содержать хотя бы одну цифру.")
        elif not any(char.isalpha() for char in password):
            print("Пароль должен содержать хотя бы одну букву.")
        else:
            print("Пароль принят.")

while True:
    print("=== МЕНЮ ===")
    print("1 - Проверить возраст")
    print("2 - Проверить email")
    print("3 - Подсчитать гласные")
    print("4 - Проверить логин и пароль")
    print("5 - Выход из программы")
    print("6 - Показать лог")
    print("7 - очистить лог")

    choise = input("Выберите действие (1-6): ")

    if  choise == "1":
        check_age()
    elif choise == "2":
        check_email()
    elif choise == "3":
        count_vowels()
    elif choise == "4":
        check_login_password()
    elif choise == "5":
        print("Выход из программы...")
        break

    elif choise == "6":
        try:
            with open("log.txt", "r", encoding="utf-8") as log_file:
                content = log_file.read()
                if content.strip() == "":
                    print("Лог пуст.")
                else:
                    print("/n=== Лог ===")
                    print(content)
        except FileNotFoundError:
            print("Файл лога еще не создан.")

    elif choise == "7":
        with open("log.txt", "w", encoding="utf-8") as log_file:
            log_file.write("")
            print("Лог очищен.")