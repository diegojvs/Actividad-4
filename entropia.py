import Hash
import sys
import hashlib

if __name__ == '__main__':
    text = sys.argv[1]
    hashmd5 = hashlib.md5(text.encode()).hexdigest()
    #print(hashmd5)
    print('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    #print("Entropia de MD5: " + str(Hash.entropia(str(hashmd5),True)))