
#funcion devuelve el porcentaje de un valor

def porcentaje(porcentaje, precio,tipo):
    if tipo == True:
        #if is true
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


#imprimir_porcentajes() #porcentual value
#print(obtener_promedio()) #average

#create menu
#version before version 3.10

def call_to_option(opt):

    options ={
         1:imprimir_porcentajes,
         2:imprimir_porcentajes,
         3:obtener_promedio,
        }

    options[opt]()


    return 



#after version 3.10
#match opt:
#            case "1":2
#                imprimir_porcentajes()
#            case "2":
#                imprimir_porcentajes()
#            case "3":
#                obtener_promedio()
#            case "4":
#                print("option 4")      
#            case _:
#                print("incorrect option")
#return
          

def print_menu():
    print("1) Porcentaje Aumento");
    print("2) Porcentaje Descuento");
    print("3) Promedio");
    print("4) Conversor de Moneda");
    print("-------------------------");
    print("0)Salir");
    return




def main_menu():
        opt = int(input("Please insert an option:"))
        #while cicle end if you put an 0 value
        print_menu()
        while opt !=0:
            call_to_option(opt)
            print_menu()
            opt = int(input("Please insert an option:"))
                
        return
        
    

main_menu()