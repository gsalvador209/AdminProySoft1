import math 
import os
import datetime

"""Program title"""
print("\t\t************")
print("\t\t\t Codificador y decodificador")
print("\t\t************")
print("\n Cervantes García Eduardo\n Chávez Villanueva Giovanni Salvador\n Rosales Piña Alejandra\n Sánchez Mendoza Carlos Omar\n Torres Bravo Cecilia\n Zurita León Dana Cecilia")

"""There is a menu for the user to enter the option to perform
To choose the option a function was made where depending on the option is what is done """
print("")
print("Menú")

print("1. Codificar")
print("2. Decodificar")
opcion = input("Ingrese el número de su opción: ")


def menu():
  if opcion == "1":
    print("Codificación")
    txt_codec = codificar(txt_prueba, a, b)
    arch(txt_codec)

  elif opcion == "2":
    print("Decodificación ")
    #Decodificar
    decodec = []
    for i in range(len(txt_codec)):
        decodec.append(ord(txt_codec[i])^decodec_a)
        decodec_a = decodec_a + b

  else:
    print("Decodificación ")
#idkwim


'''
Función para codificar la cadena

Parametros
----------
txt_prueba : str
    La cadena a codificar
a : int
    La primera clave para codificar
b : int
    La segunda clave para codificar

Return
----------
txt_codec : str
    La cadena inicial ya codificada
'''
def codificar(txt_prueba, a, b):
  #Codificar
  codec = []
  for i in range(len(txt_prueba)):
    #print(a)
    codec.append(ord(txt_prueba[i])^a)
    a=a+b
  
  #Imprimir codificado
  txt_codec = ""
  for l in codec:
    txt_codec = txt_codec + chr(l)
  print(txt_codec)

  return txt_codec

txt_prueba = input("\nIngrese la cadena a codificar: ")
a = int(input("Ingrese la primera contraseña: "))
b = int(input("Ingrese la segunda contraseña: "))
decodec_a = a

'''
Función para historial de contraseñas

Parametros
----------
contraseña : str
    La contraseña  codificada

'''
tim=datetime.datetime.now()# para obtener el dia y hora
Hor=tim.strftime('%H:%M')#convertir la hora a string
day=tim.strftime('%-d/%m/%Y')#convertir el dia a string
def arch(contrasena):
    #verificar si existe o no el archivo donde se escribira
    if os.path.isdir('/Users/alejandrarosales/Desktop/ContraC.txt'):
        file = open('/Users/alejandrarosales/Desktop/ContraC.txt', 'a')
        file.write(contrasena + "       ")#escribir la contraseña en el archivo
        file.write(Hor + ' ' + day)#escribir el dia y hora de creacion de la contraseña en el archivo
        file.write('\n')
        file.close()
    
    else:
        file = open('/Users/alejandrarosales/Desktop/ContraC.txt', 'a')
        file.write(contrasena + "       ")#escribir la contraseña en el archivo
        file.write(Hor + ' ' + day)#escribir el dia y hora de creacion de la contraseña en el archivo
        file.write('\n')
        file.close()

menu()
