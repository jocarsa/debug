debug = ""
operando1 = input("Dime el primer operando: ")

debug += str("El valor del operando 1 es:")
debug += str(operando1)
debug += str("El tipo del operando 1 es:")
debug += str(type(operando1))

operando2 = input("Dime el segundo operando: ")

print(operando1+operando2)

print("debug: "+debug)
