import Hash
import sys
import hashlib

if __name__ == '__main__':
    text = sys.argv[1]
    hashmd5 = hashlib.md5(text.encode()).hexdigest()
    hashsh1 = hashlib.sha1(text.encode()).hexdigest()
    hashsha256 = hashlib.sha256(text.encode()).hexdigest()
    hashActividad4 = Hash.hash(text)
    print("Entropia de MD5: " + str(Hash.entropia(hashmd5)))
    print("Entropia de sha1: " + str(Hash.entropia(hashsh1)))
    print("Entropia de sha256: " + str(Hash.entropia(hashsha256)))
    print("Entropia de Actividad4: " + str(Hash.entropia(hashActividad4)))
