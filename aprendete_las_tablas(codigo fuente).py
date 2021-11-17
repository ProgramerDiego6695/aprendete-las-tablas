#aprendete las tablas por diego emiliano
#¡disfruta el juego!

#importar el paquete random
import random
#definir dos listas con numeros del 1 al 10
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#crear la funcion "cuerpo"
def cuerpo():
    #crear dos variables con un numero aleatorio de las dos listas anteriores
    multiplicando = random.choice(numero)
    multiplicador = random.choice(numero2)
    #preguntar al jugador cuanto es multiplicando * multiplicador
    print("cuanto es", multiplicando, "*", multiplicador)
    #crear la variable "producto" y que sea multiplicando * multiplicador
    producto = multiplicando * multiplicador
    #pedirle al usuario la respuesta
    entrada = input()
    #convertir la variable "entrada" de un string a un numero entero
    #PD:ocurre un error si la variable "entrada" tiene una letra
    resultado = int(entrada)
    #ver si el resultado es igual a la multiplicacion
    if resultado == producto:
        #decirte si es correcto
        print("es correcto :)")
        input()
        #ejecutar la funcion "cuerpo"
        cuerpo()
    else:
        #decirte si es incorrecto
        print("era", producto, ":(")
        input()
        #ejecutar la funcion "cuerpo"
        cuerpo()
#ejecutar la funcion "cuerpo"
cuerpo()
