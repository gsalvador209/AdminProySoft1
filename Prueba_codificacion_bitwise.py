import math 

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
  elif opcion == "2":
    print("Decodificación ")
  else:
    print("Decodificación")

menu()

txt_prueba = input()
a = int(input())
b = int(input())
decodec_a = a

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

#Decodificar
decodec = []
for i in range(len(txt_codec)):
    decodec.append(ord(txt_codec[i])^decodec_a)
    decodec_a = decodec_a + b
    