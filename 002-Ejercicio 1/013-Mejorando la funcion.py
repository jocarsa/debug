
def calcula(operando1,operando2,operador):
    if type(operando1) == int and type(operando2) == int:
        pass
    else:
        print("los operadores no son correctos")
        return 0
    if operando2 == 0 and operador == "/":
        print("intento de division por cero")
        return 0
    if operador == "+":
        return operando1+operando2
    elif operador == "-":
        return operando1-operando2
    elif operador == "*":
        return operando1*operando2
    elif operador == "/":
        return operando1/operando2

def pruebaUnitaria(o1,o2,o,resultado):
    print("---------------------------")
    print("debería haber sido:")
    print(calcula(o1,o2,o))
    print("y ha sido")
    print(resultado)
    if calcula(o1,o2,o) == resultado:
        print("exito:")   
    else:
        print("fracaso:")
    print("op1:"+str(o1)+",op2:"+str(o2)+",opr:"+str(o))

pruebaUnitaria(4,3,"+",7)
pruebaUnitaria(4,3,"-",1)
pruebaUnitaria(4,3,"*",12)
pruebaUnitaria(4,3,"/",4/3)
pruebaUnitaria(999999999999999,566634634653465,"+",1566634634653464)
pruebaUnitaria(0,0,"+",0)
pruebaUnitaria("lagarto","cerveza","/",0)
pruebaUnitaria(0,0,"/",0)


