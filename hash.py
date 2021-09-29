import time
import random

def bin_to_number(binary):
    posicion = 0
    decimal = 0
    binary = binary[::-1]
    for digito in binary:
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def hash(text):
    otracosa = 0
    semilla = int(time.time() * 10000)
    nose = random.randint(1,4)
    
    if nose == 1:
        otracosa = semilla + (nose * random.randint(1,100))
    elif nose == 2:
        otracosa = semilla - (nose * random.randint(1,100))
    elif nose == 3:
        otracosa = semilla / (nose * random.randint(1,100))
    else:
        otracosa = semilla * (nose * random.randint(1,50))
    
    return  int(otracosa)

if __name__ == '__main__':
    text = 'ño'
    x = 0
    for byte in text:
        int_value = ord(byte)
        bits = '{0:08b}'.format(int_value)
        algo = bin_to_number(bits)
        x += hash(algo)
    print((str(x).encode("utf-8")).hex())
