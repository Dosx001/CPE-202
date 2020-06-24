from huffman import *
import subprocess
from random import randrange as rand

for i in range(256):
    fp=open('chr.txt','w')
    for i in range(rand(25)):
        fp.write(chr(rand(256)))
    fp.close()
    huffman_encode('chr.txt','chr_out.txt')
    huffman_decode('chr_out.txt','chr_decoded.txt')
    err = subprocess.call("diff -wb chr_decoded.txt chr.txt", shell = True)
    if err!=0:
        print(chr(i),i,err)
        break
    else:
        print('Good') 
     
