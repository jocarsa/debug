debug = ""
operando1 = input("Dime el primer operando: ")
operando1 = int(operando1)
operando2 = input("Dime el segundo operando: ")
operando2 = int(operando2)

print(operando1+operando2)

debug += str("El valor del operando 1 es:")
debug += str(operando1)
debug += str("El tipo del operando 1 es:")
debug += str(type(operando1))
print("debug: "+debug)
