import Hash
import fileinput
import hashlib

if __name__ == '__main__':
    data = []
    count = 0
    for lines in fileinput.input(): # Se carga cada palabra en un arreglo para completar las pruebas
        data.append(lines.rstrip())
        count += 1
        if count == 50:
            break
    
    print("----------MD5----------")
    for word in data:
        print(word + ": " + str(hashlib.md5(word.encode()).hexdigest()))
    print("")

    print("----------SHA1----------")
    for word in data:
        print(word + ": " + str(hashlib.sha1(word.encode()).hexdigest()))
    print("")

    print("----------SHA256----------")
    for word in data:
        print(word + ": " + str(hashlib.sha256(word.encode()).hexdigest()))
    print("")

    print("----------Actividad-4----------")
    for word in data:
        print(word + ": " + str(Hash.hash(word)))
