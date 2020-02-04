import numpy as np
from PIL import Image

img = Image.open("Untitled.png")
img = np.array(img)

picres = 600
tff = np.zeros((picres,picres), dtype="uint8")
fftres = 600
scale = 1/(picres**2)
fftq = int(fftres/2)
tffo = np.zeros((fftres, fftres))
remove = np.zeros((150, 150))


for x in range(picres):
    for y in range(picres):
        tff[x][y] = img[x][y][0]
fft1 = np.fft.fft2(tff, s = (fftres,fftres))
fft = abs(fft1.imag*fft1.real*scale)
for x in range(150):
    for y in range(150):
        if True:# x <150 and x>=0 and y<150 and y>=0:
            remove[x][y] = fft1[x][y]
for xquad in range(2):
    for yquad in range(2):
        for x in range(xquad*fftq, fftq*(xquad+1)):
            for y in range(yquad*fftq, fftq*(yquad+1)):
                if xquad == 0 and yquad == 0:
                    tffo[x+fftq][y+fftq] = fft[x][y]
                if xquad == 1 and yquad == 0:
                    tffo[x-xquad*fftq][y+fftq] = fft[x][y]
                if xquad == 0 and yquad == 1:
                    tffo[x+fftq][y-yquad*fftq] = fft[x][y]
                if xquad == 1 and yquad == 1:
                    tffo[x-xquad*fftq][y-yquad*fftq] = fft[x][y]
# abs(tffo*scale)

result = Image.fromarray(tffo.astype(np.uint8))#.convert('RGB')
im1 = result.save("zzz.png")

tffo = np.fft.ifft2(remove, s = (picres,picres))
result = Image.fromarray(tffo.astype(np.uint8))#.convert('RGB')
im1 = result.save("zzzz.png")

    


    

    

