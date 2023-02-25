import math

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
    

#Imprimir decodificado
txt_decodec = ""
for l in decodec:
    txt_decodec = txt_decodec + chr(l)
print(txt_decodec)

