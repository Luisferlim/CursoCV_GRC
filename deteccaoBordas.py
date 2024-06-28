import cv2 as cv
import numpy as np

img = cv.imread('Fotos/ufc.jpg')
cv.imshow('ufc', img)

dog = cv.imread("Fotos/dogs.jpg")
cv.imshow('dogs', dog)

cinza = cv.cvtColor(dog, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', dog)

#laplaciano
lap = cv.Laplacian(cinza, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplaciana', lap)

#sobel (gradiente[loucura])
sobelx = cv.Sobel(cinza, cv.CV_64F, 1, 0)
cv.imshow('sobel x', sobelx)
sobely = cv.Sobel(cinza, cv.CV_64F, 0, 1)
cv.imshow('sobel y', sobely)

sobel_combinado = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel combinado', sobel_combinado)

#canny
canny = cv.Canny(cinza, 150, 175)
cv.imshow("canny", canny)


cv.waitKey(0)
cv.destroyAllWindows()