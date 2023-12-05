
def calcula(operando1,operando2,operador):
    if operador == "+":
        return operando1+operando2
    elif operador == "-":
        return operando1+operando2
    elif operador == "*":
        return operando1*operando2
    elif operador == "/":
        return operando1/operando2

def pruebaUnitaria(o1,o2,o,resultado):
    if calcula(o1,o2,o) == resultado:
        print("exito:")
    else:
        print("fracaso:")
    print("op1:"+o1+",op2:"+o2+",opr:"+o)




