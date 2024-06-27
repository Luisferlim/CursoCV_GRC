import cv2 as cv
import numpy as np

img = cv.imread("Fotos/ufc.jpg")
cv.imshow("ufc", img)

vazio = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("vazio", vazio)

b,g,r = cv.split(img)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

azul = cv.merge([b,vazio,vazio])
verde = cv.merge([vazio, g,vazio])
vermelho = cv.merge([vazio, vazio, r])

cv.imshow('azul', azul)
cv.imshow('vermelho', vermelho)
cv.imshow('verde', verde)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
print(cinza.shape)

juntar = cv.merge([b,g,r])
cv.imshow('juntar', juntar)

#ver as dimensoes do hsv e LAB

cv.waitKey(0)
cv.destroyAllWindows()