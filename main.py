from PIL import Image
from DCT import twoddct

img=Image.open("image.JPG").convert("L")
pixels=list(img.getdata())
width,height=img.size
matrix=[pixels[i*width:(i+1)*width]for i in range(height)]
matrix = [[matrix[i][j] - 128.0 for j in range(width)] for i in range(height)]
blocks = []
for i in range(0, height-7, 8):
    for j in range(0, width-7, 8):
        block = [matrix[i+r][j:j+8] for r in range(8)]
        blocks.append(block)
nblocks=len(blocks)
p = [[0.0] * 8 for i in range(8)]
for block in blocks:
    coeff=twoddct(block)
    for k in range(8):
        for l in range(8):
            p[k][l]+=coeff[k][l]**2
for k in range(8):
        for l in range(8):
            p[k][l]/=nblocks

print("P[0][0]:", p[0][0])
print("P[7][7]:", p[7][7])
for rows in p:
     print([round(v,2) for v in rows])