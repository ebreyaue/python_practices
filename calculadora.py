
#funcion devuelve el porcentaje de un valor

def porcentaje(porcentaje, precio,tipo):
    if tipo == True:
        #si el aumento es true
        porcentaje = porcentaje+1
    else:
        porcentaje=1.0-porcentaje    
    
    valor=(precio * float(porcentaje)) 
    return valor



def imprimir_porcentajes():
    prs = 0.2 #porcentaje del 20%
    precio=float(input("Ingrese Precio:"))
    print("precio con un",prs,"% de Aumento")
    print(int(porcentaje(float(prs), precio,1))) #me imprime el valor con aumento
    print("precio con un",prs,"% de Descuento")
    print(int(porcentaje(float(prs), precio,0))) #me imprime el valor con descuento
    return

def obtener_promedio():
        suma=0 #asignar el valor 0 para que no me devuelva basura.
        counter=0 #contador
        valor = float(input("Ingrese Valor:"))
        #generar un ciclo while que solo cierra al ingresar 0
        while valor !=0:
            suma+=valor
            counter+=1
            valor = float(input("Ingrese Valor:"))
        return int(suma/counter)
#imprimir_porcentajes()

print(obtener_promedio())