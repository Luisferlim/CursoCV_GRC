import cv2 as cv
import numpy as np

vazio = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('vazio', vazio)

#pintar

#verde #BGR
vazio[:] = 0,255,0
cv.imshow("verde", vazio)

#azul
vazio[:] = 255,0,0
cv.imshow("azul", vazio)

#vermelho
vazio[:] = 0,0,255
cv.imshow("vermelho", vazio)

#branco
vazio[:] =255,255,255
cv.imshow("branco?", vazio)

#quadrado vermelho
vazio[200:300, 300:400] = 0,0,255
cv.imshow("bloco", vazio)

vazio = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('vazio2', vazio)

#retangulo
cv.rectangle(vazio, (10,10), (vazio.shape[1]//2, vazio.shape[0]//2), (0,255,0), thickness=1)
cv.imshow('retangulo', vazio)

#circulo
cv.circle(vazio, (255,255), 50, (0,0,255), -1) #circulo preenchido
cv.imshow("circulo", vazio)

#desenho de linha
cv.line(vazio, (0,0), (500,500), (255,255,255), 2)
cv.imshow('linha', vazio)

#texto 
cv.putText(vazio, 'grenal', (0,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), 2)
cv.imshow('texto', vazio)


cv.waitKey(0)
cv.destroyAllWindows()
