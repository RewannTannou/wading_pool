numero = int(input("donner un numéro :"))
charNumero = str(numero)

if charNumero[-1] == "0" or charNumero[-1] == "2" or charNumero[-1] == "4" or charNumero[-1] == "6" or charNumero[-1] == "8" :
    print("this number is odd")
else : 
    print("even")

