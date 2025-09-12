numero = int(input("number plz : "))
charNumero = str(numero)
if numero == 42 :
    print("a")
else :
    if numero <= 21:
        print("b")
    else:
        if charNumero[-1] == "1" or charNumero[-1] == "3" or charNumero[-1] == "5" or charNumero[-1] == "7" or charNumero[-1] == "9" :
            print("even")
        else:
            if numero/2 < 21:
                print("d")
            else :
                if charNumero[-1] == "0" or charNumero[-1] == "2" or charNumero[-1] == "4" or charNumero[-1] == "6" or charNumero[-1] == "8" and numero >= 45 :
                    print("e")
                else:
                    print("f")