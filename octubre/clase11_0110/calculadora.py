def calculadora():
    while True:
        try:
            num1 = float(input("Primer número: "))
            operaction = input("Operación (+, -, *, /): ")
            num2 = float(input("Segundo número: "))

            if operaction == "+":
                result = num1 + num2
            elif operaction == "-":
                result = num1 - num2
            elif operaction == "*":
                result = num1 * num2
            elif operaction == "/":
                result = num1 / num2
            else:
                print("Operación no válida")
                continue
            print(f"Result: {result}")
            break
        except ValueError:
            print("Error: Ingrese números válidos")
        except ZeroDivisionError:
            print("Error: no se puede dividir por cero")
        except KeyboardInterrupt:
            print("Operación cancelada")
            break

calculadora()
