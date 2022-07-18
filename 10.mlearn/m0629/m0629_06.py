from cProfile import label
import urllib.request as req
import gzip, os, os.path
import struct

# img_f=open('./10.mlearn/mnist/train-images-idx3-ubyte','rb')
# lbl_f=open('./10.mlearn/mnist/train-labels-idx1-ubyte','rb')
img_f=open('./10.mlearn/mnist/t10k-images-idx3-ubyte','rb')
lbl_f=open('./10.mlearn/mnist/t10k-labels-idx1-ubyte','rb')

# csv_f = open('./10.mlearn/mnist/train.csv','w',encoding='utf-8')
csv_f = open('./10.mlearn/mnist/test.csv','w',encoding='utf-8')

mag,lbl_count = struct.unpack(">II",lbl_f.read(8))
mag,img_count = struct.unpack(">II",img_f.read(8))
rows, cols = struct.unpack(">II",img_f.read(8))
pixels = rows * cols 

for idx in range(lbl_count):
    if idx > 1000:break
    label = struct.unpack("B",lbl_f.read(1))[0]
    bdata = img_f.read(pixels)
    sdata = list(map(lambda a: str(a),bdata))
    csv_f.write(str(label)+",")
    csv_f.write(",".join(sdata)+"\r\n")
    
csv_f.close()
lbl_f.close()
img_f.close()
print("csv파일 생성완료")