import sys
import re
from math import log

def resolver(numero): # Se realizan operaciones matematicas para mantener el numero ASCII entre 33 y 126
    while numero < 33 or numero > 126:
        if numero < 33:
            numero = abs(numero + int(numero/2))
        elif numero > 126:
            numero = abs(numero - int(numero/2))
        else:
            break
    return numero

def resolver2(numero): # Se realizan operaciones matematicas para mantener el numero ASCII entre 33 y 126
    while numero < 33 or numero > 126:
        if numero < 33:
            numero = abs(numero + int(numero/3))
        elif numero > 126:
            numero = abs(numero - int(numero/3))
        else:
            break
    return numero

def hash(text): # Funcion que calcula el hash
    hashByte = bytearray(25) # Se inicia una lista de bytes
    sum = 0
    for i in text: # Se obtiene el numero ASCII y se obtiene la suma total
        sum += ord(i)
        
    if sum > 32 and sum < 127: # Si esta entre 33 y 126 se agrega al primer elemento de la lista
        hashByte[0] = sum
    else: # Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
        hashByte[0] = resolver(sum)
    
    for j in range(1,6): # Se hacen operaciones matematicas para los siguientes 5 elementos de la lista
        if int(hashByte[j-1]/3) * 7 > 32 and int(hashByte[j-1]/3) * 7 < 127: # Si la operacion matematica esta entre 33 y 126 se agrega el elemento a lista
            hashByte[j] = int(hashByte[j-1]/3) * 7 
        else:# Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
            hashByte[j] = resolver(int(hashByte[j-1]/3) * 7)

    for k in range(6,11): # Se hacen operaciones matematicas para los siguientes 5 elementos de la lista
        if hashByte[k-6] + hashByte[k-4] + hashByte[k-2] > 32 and hashByte[k-6] + hashByte[k-4] + hashByte[k-2] < 127: # Si la operacion matematica esta entre 33 y 126 se agrega el elemento a lista
            hashByte[k] = hashByte[k-6] + hashByte[k-4] + hashByte[k-2]
        else: # Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
            hashByte[k] = resolver2(hashByte[k-6] + hashByte[k-4] + hashByte[k-2])
    
    acumulado = 0
    for b in range(0,11):
        acumulado += hashByte[b]
    for l in range(11,16): # Se hacen operaciones matematicas para los siguientes 5 elementos de la lista
        if int(acumulado%33 + hashByte[l-7]) > 32 and int(acumulado%33 + hashByte[l-7]) < 127: # Si la operacion matematica esta entre 33 y 126 se agrega el elemento a lista
            hashByte[l] = int(acumulado%33 + hashByte[l-7]) 
        else: # Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
            hashByte[l] = resolver(int(acumulado%33 + hashByte[l-7]))
    
    for m in range(16,20): # Se hacen operaciones matematicas para los siguientes 5 elementos de la lista
        if int(abs(acumulado - hashByte[m-7])) > 33 and int(abs(acumulado - hashByte[m-7])) < 127: # Si la operacion matematica esta entre 33 y 126 se agrega el elemento a lista
            hashByte[m] = int(abs(acumulado - hashByte[m-7]))
        else: # Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
            hashByte[m] = resolver2(int(abs(acumulado - hashByte[m-7])))
    
    for n in range(20,25): # Se hacen operaciones matematicas para los siguientes 4 elementos de la lista
        if int((hashByte[n-1]/2)*5) > 33 and int((hashByte[n-1]/2)*5) < 127: # Si la operacion matematica esta entre 33 y 126 se agrega el elemento a lista
            hashByte[n] = int((hashByte[n-1]/2)*5)
        else: # Si no esta entre esos rangos se llama a una funcion para que retorne un numero entre ese rango
            hashByte[n] = resolver2(int((hashByte[n-1]/2)*5))
    
    return hashByte.decode("utf-8")

def entropia(texto,): # Calculo de la entropia mediente la diferencia entre el numero ASCII mas alto y el numero ASCII mas bajo de un texto
    entropia = 0
    base = 0
    if re.search('[a-f]',texto) != None and re.search('[g-z]',texto) == None:
        base += 6
        if re.search('[0-9]',texto) != None:
            base += 10
        entropia = len(texto)*log(base,2)
    elif re.search('[a-zA-Z]',texto) != None:
        base += 52
        if re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]',texto) != None:
            base += 32
            if re.search('[0-9]',texto) != None:
                base += 10
        entropia = len(texto)*log(base,2)    
    print("base:", base)
    print("Largo:", len(texto))
    return entropia


if __name__ == '__main__':
    data = []
    if sys.argv[1] == "-h": # Argumento para calcular el hash para un solo texto
        data.append(sys.argv[2])
        for palabra in data:
            print("Hash: " + hash(palabra)) # Por cada palabra se calcula un hash
    
    elif sys.argv[1] == "-f": # Argumento para calcular el hash para de los textos que están dentro de un archivo txt
        with open(sys.argv[2]) as f: # Abre el archivo
            for line in f:
                data.append(line.rstrip())
        for palabra in data:
            print("Hash: " + hash(palabra)) # Por cada palabra se calcula un hash
    
    elif sys.argv[1] == "-he": # Argumento para calcular el hash y la entropia para un solo texto
        data.append(sys.argv[2])
        for palabra in data:
            palabraHash = hash(palabra) # Por cada palabra se calcula un hash
            print("Hash: " + palabraHash) 
            print("Entropia: " + str(entropia(palabraHash))) # Calcula e imprime la entropia
    
    elif sys.argv[1] == "-fe": # Argumento para calcular el hash y la entropia de los textos que están dentro de un archivo txt
        with open(sys.argv[2]) as f: # Abre el archivo
            for line in f:
                data.append(line.rstrip())
        for palabra in data:
            palabraHash = hash(palabra) # Por cada palabra se calcula un hash
            print("Hash: " + palabraHash)
            print("Entropia: " + str(entropia(palabraHash))) # Calcula e imprime la entropia
    
    elif sys.argv[1] == "-e": # Argumento para calcular la entropia para un solo texto
        data.append(sys.argv[2])
        for palabra in data:
            palabraHash = hash(palabra)
            print("Entropia: " + str(entropia(palabraHash))) # Calcula e imprime la entropia
    
    elif sys.argv[1] == "-ef":# Argumento para calcular la entropia de los textos que están dentro de un archivo txt
        with open(sys.argv[2]) as f: # Abre el archivo
            for line in f:
                data.append(line.rstrip())
        for palabra in data:
            palabraHash = hash(palabra)
            print("Entropia: " + str(entropia(palabraHash))) # Calcula e imprime la entropia
    
    else:
        print("No se uso el formato")
