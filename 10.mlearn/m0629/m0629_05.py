import urllib.request as req
import gzip, os, os.path

savepath='./10.mlearn/mnist'
baseurl = 'http://yann.lecun.com/exdb/mnist'

files = [
    'train-images-idx3-ubyte.gz',
'train-labels-idx1-ubyte.gz',
't10k-images-idx3-ubyte.gz',
't10k-labels-idx1-ubyte.gz' ]
# http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
if not os.path.exists(savepath): os.makedirs(savepath)

# for f in files:
#     url = baseurl+"/"+f
#     loc = savepath+"/"+f
#     if not os.path.exists(loc):
#         req.urlretrieve(url, loc)

for f in files:
    url=baseurl+"/"+f
    loc=savepath+"/"+f
    if not os.path.exists(loc):
        #파일 다운로드 저장시킴 : urlretrive(가져올 url, 파일 저장 위치)-파일 저장
        req.urlretrieve(url,loc)
    
#gzip 압축해제
for f in files:
    gz_file=savepath+"/"+f
    raw_file=savepath+"/"+f.replace(".gz","")
    with gzip.open(gz_file,"rb")as fp:
        body = fp.read()
        with open(raw_file,"wb")as w:
            w.write(body)
            
print('저장완료')