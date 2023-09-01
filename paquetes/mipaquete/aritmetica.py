def suma(a1,a2):
    c=a1+a2
    return c

def resta(a1,a2):
    c=a1-a2
    return c

def multipli(a1,a2):
    c=a1*a2
    return c

def division(a1,a2):
    c=a1/a2
    return c

def calc(a1,a2,operator):
    if(operator=="suma"):
        c = suma(a1,a2)
    elif(operator=="resta"):
        c = resta(a1,a2)
    elif(operator=="multipli"):
        c = multipli(a1,a1)
    else:
        c = division(a1,a2)
    return f"El resultado de la {operator} es: {c}"
    