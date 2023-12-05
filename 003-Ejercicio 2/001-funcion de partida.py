def calcula(operando1,operando2,operador):
    print("el operando 1 es:"+str(operando1))
    print("el operando 2 es:"+str(operando2))
    print("el operador es:"+str(operador))
    if type(operando1) == int and type(operando2) == int:
        pass
    else:
        print("los operadores no son correctos")
        return 0
    if operando2 == 0 and operador == "/":
        print("intento de division por cero")
        return 0
    print("Ahora lo que se ha calculado es:")
    if operador == "+":
        print(operando1+operando2)
        return operando1+operando2
    elif operador == "-":
        print(operando1-operando2)
        return operando1-operando2
    elif operador == "*":
        print(operando1*operando2)
        return operando1*operando2
    elif operador == "/":
        print(operando1/operando2)
        return operando1/operando2

print(calcula(4,3,"-"))
    


