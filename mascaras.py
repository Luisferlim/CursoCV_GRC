import cv2 as cv
import numpy as np

img = cv.imread('Fotos/ufc.jpg')
cv.imshow("ufc", img)

vazio = np.zeros(img.shape[:2], dtype='uint8')

#mascara
mascara = cv.circle(vazio.copy(), (img.shape[1]//2 + 27, img.shape[0]//2), 100, 255, -1)
cv.imshow('mascara', mascara)

#mascara2
mascara2 = cv.rectangle(vazio.copy(), (40,40), (400,400), 255, -1)
cv.imshow('mascara2', mascara2)

#imagem mascarada
mascarado = cv.bitwise_and(img, img, mask=mascara)
cv.imshow('mascarado', mascarado)

#imagem mascarada2
mascarado2 = cv.bitwise_and(img, img, mask=mascara2)
cv.imshow('mascarado2', mascarado2)

cv.waitKey(0)
cv.destroyAllWindows()