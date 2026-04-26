from descuento import aplicar_descuento

def main():
    intentos = 0
    while intentos < 3:
        print("Sistema de descuentos")
        try:
            edad = int(input("Ingrese su edad: "))
            precio = float(input("Ingrese el precio: "))
            if edad < 0 or precio < 0:
                raise ValueError
        except ValueError:
            print("Datos invalidos. Ingresa numeros positivos")
            continue
        cupon = input("Ingrese cupon disponible: ").upper()
        intentos += 1

        resultado = aplicar_descuento(precio, edad, cupon, intentos)

        if isinstance(resultado, str):
            print(f"Intentos restantes: {3 - intentos}")
            print(resultado)
            if "Bloqueado" in resultado:
                break
            continue
        else:
            print(f"Precio final con descuento: ${resultado}")
            break
            
if __name__ == "__main__":
    main()