while True:
    try:
        num1 = float(input("Birinchi sonni kiriting: "))
        num2 = float(input("Ikkinchi sonni kiriting: "))
        operator = input("Amalni kiriting (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Nolga bo'lish mumkin emas!")
            result = num1 / num2
        else:
            print("Noto'g'ri amal kiritildi!")
            continue

        print(f"Natija: {result}")
        break  # To'g'ri bajarilganidan keyin loopdan chiqamiz

    except ValueError:
        print("Noto'g'ri son kiritildi!")
    except ZeroDivisionError as e:
        print(e)
