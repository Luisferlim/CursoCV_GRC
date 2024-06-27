import cv2 as cv
import numpy as np

img = cv.imread('Fotos/ufc.jpg')
cv.imshow('ufc', img)

vazio = np.zeros(img.shape, dtype='uint8')
cv.imshow('vazio', vazio)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', cinza)

#suavizacao
blur = cv.GaussianBlur(cinza, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#canny
canny = cv.Canny(blur, 10, 175)
cv.imshow("canny", canny)

#binarizacao
ret, thresh = cv.threshold(cinza, 150, 255, cv.THRESH_BINARY)
cv.imshow("binario", thresh)

#contorno
contornos, hierarquias = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contornos)} contornos encontrados')

cv.drawContours(vazio, contornos, -1, (0,0,255), 1)
cv.imshow('contornos', vazio)

cv.waitKey(0)
cv.destroyAllWindows()