import math 
import os
import datetime

def menu(opcion,a,b,txt_tocodec):

  if opcion == "1":
    print("Codificación")
    txt_codec = codificar(txt_tocodec, a, b)
    arch(txt_codec)
    
  elif opcion == "2":
        print("Decodificación ")
        #Decodificar
        txt_decodec = decodificar(txt_tocodec,a, b)
        



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

  '''
Función para decodificar la cadena
Parametros
----------------------------------
txt_codec : str
    La cadena ya codificada
a : int
    La primera clave para codificar
b : int
    La segunda clave para codificar
Return
----------------------------------
txt_decodec : str
    La cadena ya decodificada
'''
def decodificar(txt_codec, decoded_a, b):
  #Decodificar
  decodec = []
  for i in range(len(txt_codec)):
    decodec.append(ord(txt_codec[i])^decoded_a)
    decoded_a =  decoded_a + b
  
  # Imprimir decodificado
  txt_decodec = ""
  for l in decodec:
    txt_decodec = txt_decodec + chr(l)
  print(txt_decodec)
  
  return txt_decodec


'''
Función para leer un archivo de texto y pasarlo a cadena

Parametros
----------
txt_nombre : str
    nombre del arhivo a codificar o su directorio en la computadora

Return
----------
txt_tocodec : str
    texto del archivo en formato de cadena para codificar
'''
def read_txt_file(txt_nombre):
    
    #Verificar si es nombre o directorio
    tocompare=""
    for i in range(1,3):
      tocompare=tocompare+txt_nombre[i]
    
    #Abrir archivo dependiendo de si de dio un nombre o directorio
    if(tocompare==":\\"):
        with open(txt_nombre,"a") as file_object:
          txt_tocodec=file_object.read()
    else:
      with open(txt_nombre+".txt","a") as file_object:
        txt_tocodec=file_object.read()

    print("El texto a codificar es:\n"+txt_tocodec)
    return txt_tocodec
    # txt_nombre = dir + "Prueba d.txt"
    # file = open(txt_nombre, '+a')
    # txt_tocodec= file.readline()
    # file.close()


'''
Función para historial de contraseñas

Parametros
----------
contraseña : str
    La contraseña  codificada

'''

def arch(contrasena):
    direct = os.getcwd()
    tim=datetime.datetime.now()# para obtener el dia y hora
    Hor=tim.strftime('%H:%M')#convertir la hora a string
    day=tim.strftime("%d/%m/%Y")#convertir el dia a string
    #verificar si existe o no el archivo donde se escribira
    if os.path.isdir(direct + "\\" +'ContraC.txt'):
        print(direct + "\\" +'ContraC.txt')
        file = open(direct + "\\" +'ContraC.txt', 'a')
        file.write(contrasena + "       ")#escribir la contraseña en el archivo
        file.write(Hor + ' ' + day)#escribir el dia y hora de creacion de la contraseña en el archivo
        file.write('\n')
        file.close()
    
    else:
        file = open(direct + "\\" +'ContraC.txt', 'a')
        file.write(contrasena + "       ")#escribir la contraseña en el archivo
        file.write(Hor + ' ' + day)#escribir el dia y hora de creacion de la contraseña en el archivo
        file.write('\n')
        file.close()

def main():
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

  #txt_nombre=input("\nIngrese el nombre del archivo a codificar o el directorio del archivo:")
  print("Ingresa el texto")
  txt_tocodec=input()
  a = int(input("Ingrese la primera contraseña: "))
  b = int(input("Ingrese la segunda contraseña: "))

  menu(opcion,a, b,txt_tocodec)

main()