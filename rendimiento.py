import hashlib
import time
import Hash
import fileinput

if __name__ == '__main__':
    data = []
    tiempoMD5 = []
    count = 0
    for lines in fileinput.input(): # Se carga cada palabra en un arreglo para completar las pruebas
        data.append(lines.rstrip())
        count += 1
        if count == 81:
            break
    Prueba1MD5 = time.time() # Inicio en de las pruebas para MD5
    for i in range(0,81):
        h = data[i]
        hashlib.md5(h.encode())
        if i == 0: # Prueba 1
            tiempoMD5.append((time.time() - Prueba1MD5)*1000)
            Prueba2MD5 = time.time()
        elif i == 10: # Prueba 2
            tiempoMD5.append((time.time() - Prueba2MD5)*1000)
            Prueba3MD5 = time.time()
        elif i == 30: # Prueba 3
            tiempoMD5.append((time.time() - Prueba3MD5)*1000)
            Prueba4MD5 = Prueba3MD5 = time.time()
        elif i == 80: # Prueba 4
            tiempoMD5.append((time.time() - Prueba4MD5)*1000)
    print("Tiempos MD5:" , tiempoMD5)
    
    tiempoSHA1 = []
    Prueba1SHA1 = time.time() # Inicio en de las pruebas para SHA1
    for i in range(0,81):
        h = data[i]
        hashlib.sha1(h.encode())
        if i == 0: # Prueba 1
            tiempoSHA1.append((time.time() - Prueba1SHA1)*1000)
            Prueba2SHA1 = time.time()
        elif i == 10: # Prueba 2
            tiempoSHA1.append((time.time() - Prueba2SHA1)*1000)
            Prueba3SHA1 = time.time()
        elif i == 30: # Prueba 3
            tiempoSHA1.append((time.time() - Prueba3SHA1)*1000)
            Prueba4SHA1 = Prueba3SHA1 = time.time()
        elif i == 80: # Prueba 4
            tiempoSHA1.append((time.time() - Prueba4SHA1)*1000)
    print("Tiempos SHA1:" , tiempoSHA1)

    tiempoSHA256 = []
    Prueba1SHA256 = time.time() # Inicio en de las pruebas para SHA256
    for i in range(0,81):
        h = data[i]
        hashlib.sha256(h.encode())
        if i == 0: # Prueba 1
            tiempoSHA256.append((time.time() - Prueba1SHA256)*1000)
            Prueba2SHA256 = time.time()
        elif i == 10: # Prueba 2
            tiempoSHA256.append((time.time() - Prueba2SHA256)*1000)
            Prueba3SHA256 = time.time()
        elif i == 30: # Prueba 3
            tiempoSHA256.append((time.time() - Prueba3SHA256)*1000)
            Prueba4SHA256 = Prueba3SHA256 = time.time()
        elif i == 80: # Prueba 4
            tiempoSHA256.append((time.time() - Prueba4SHA256)*1000)
    print("Tiempos SHA256:" , tiempoSHA256)

    tiempoActividad4 = []
    Prueba1Actividad4 = time.time() # Inicio en de las pruebas para Actividad4
    for i in range(0,81):
        Hash.hash(data[i])
        if i == 0: # Prueba 1
            tiempoActividad4.append((time.time() - Prueba1Actividad4)*1000)
            Prueba2Actividad4 = time.time()
        elif i == 10: # Prueba 2
            tiempoActividad4.append((time.time() - Prueba2Actividad4)*1000)
            Prueba3Actividad4 = time.time()
        elif i == 30: # Prueba 3
            tiempoActividad4.append((time.time() - Prueba3Actividad4)*1000)
            Prueba4Actividad4 = Prueba3Actividad4 = time.time()
        elif i == 80: # Prueba 4
            tiempoActividad4.append((time.time() - Prueba4Actividad4)*1000)
    print("Tiempos Actividad-4:" , tiempoActividad4)
