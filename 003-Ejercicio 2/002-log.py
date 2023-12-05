def calcula(operando1,operando2,operador):
    archivo = open("log.txt","w")
    cadena = ""
    cadena += "el operando 1 es:"+str(operando1)
    cadena += "el operando 2 es:"+str(operando2)
    cadena += "el operador es:"+str(operador)
    if type(operando1) == int and type(operando2) == int:
        pass
    else:
        cadena += "los operadores no son correctos"
        return 0
    if operando2 == 0 and operador == "/":
        cadena += "intento de division por cero"
        return 0
    print("Ahora lo que se ha calculado es:")
    if operador == "+":
        cadena += str(operando1+operando2)
        archivo.write(cadena)
        archivo.close()
        return operando1+operando2
    elif operador == "-":
        cadena += str(operando1-operando2)
        archivo.write(cadena)
        archivo.close()
        return operando1-operando2
    elif operador == "*":
        cadena += str(operando1*operando2)
        archivo.write(cadena)
        archivo.close()
        return operando1*operando2
    elif operador == "/":
        cadena += str(operando1/operando2)
        archivo.write(cadena)
        archivo.close()
        return operando1/operando2
    

print(calcula(4,3,"-"))
    


