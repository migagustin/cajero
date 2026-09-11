from cuenta import Cuenta

pin_correcto = 6767
intentos = 0
saldo = 676767
dinero_cajero = 999999

cuenta = Cuenta("123456", saldo)
saldoactual = cuenta.consultarSaldo()
print(f'el saldo es de: {saldoactual}')

while intentos < 3:
    pin = int(input("ingresa su pin: "))
    if pin == pin_correcto:
        print("pin correcto")
        break
    else:
        intentos = intentos + 1
        print("pin incorrecto ✖︎")

if intentos == 3:
    print("tarjeta bloqueada")

else:
    print("\nbienvenido al cajero\n")
    print("1 sonsultar saldo")
    print("2 extraer dinero")
    print("3 realizar transferencia")

    opcion = int(input("Seleccione una operación: "))

    if opcion == 1:
        print("tu saldo es:", saldo)

    elif opcion == 2:
        monto = int(input("ingresa el monto a extraer: "))

        if monto > saldo:
            print("no tenes saldo suficiente")

        elif monto > dinero_cajero:
            print("el cajero no tiene dinero")

        elif monto > 300000:
            print("el monto maximo por es $300000")

        elif monto % 1000 != 0:
            print(" melonto debe ser múltiplo de $1000")

        else:
            saldo = saldo - monto
            dinero_cajero = dinero_cajero - monto

            print("retira el dinero")
            print("tu nuevo saldo es:", saldo)


    elif opcion == 3:
        cuenta_destino = input("ingresa la cuenta de destino: ")
        monto = int(input("ingresa el monto a transferir: "))

        if monto > saldo:
            print("no hay saldo suficiente")

        elif monto <= 0:
            print("el monto debe ser mayor a 0")

        else:
            saldo = saldo - monto

            print("transferencia hecha ✔︎✔︎✔︎✔︎✔︎✔︎")
            print("cuenta destino:", cuenta_destino)
            print("monto transferido:", monto)
            print("tu nuevo saldo es:", saldo)

    else:
        print("opcion incorrecta ✖︎")