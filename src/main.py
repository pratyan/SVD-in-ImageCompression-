import numpy as np
from numpy.linalg import svd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def rank(a, b, limit):
    arr = []

    for i in range(limit):
        print(i)
        temp = []

        for j in range(len(a)):
            t = []

            for k in range(len(b[0])):
                t.append(a[j][i]*b[i][k])

            temp.append(t)

        arr.append(temp)

    return arr
    

img = mpimg.imread('5400.png')     
gray = rgb2gray(img)    


#gray = [[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[0,1,1,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]]


def inverted(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            gray[i][j] = 1-g[i][j]
                
    return g



I = np.array(inverted(gray))
plt.imshow(I, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

SVD = svd(I)
mua = np.array(rank(SVD[0], SVD[2], len(SVD[1])))

def res(n):
    temp = mua[0]*SVD[1][0]

    for i in range(n):
        if i != 0:
            temp += mua[i]*SVD[1][i]


    plt.imshow(temp, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()


    

 


