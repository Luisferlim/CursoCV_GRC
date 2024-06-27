import cv2 as cv
import numpy as np

img = cv.imread('Fotos/dog.webp')
cv.imshow('doguinho', img)

#transladar
def translada(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensoes = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensoes)

# x direita
# -x esquerda
# y baixo
# -y cima

transladado = translada(img, 100, 100)
cv.imshow('translado', transladado)

transladado2 = translada(img, -100, 100)
cv.imshow('translado2', transladado2)

#rotacao
def rodar(img, teta, pontoRot = None):
    (altura, largura) = img.shape[:2]

    if pontoRot == None:
        pontoRot = (largura//2, altura//2)

    rotMat = cv.getRotationMatrix2D(pontoRot, teta, 1.0)
    dimensoes =(largura, altura)

    return cv.warpAffine(img, rotMat, dimensoes)

rotacionada = rodar(img, 45, pontoRot=(10,10))
cv.imshow('rotacionada', rotacionada)

#mudanca de tamanha/escala resizing 
#alargar inter_cubic e inter _linear diminuir (shrink) inter_area
mudatamanho =cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('tamanho reduzido', mudatamanho)

#fliping (inversao)
flip = cv.flip(img, -1) #o vertical, 1 e -1 horizontais
cv.imshow('inversao', flip)

cv.waitKey(0)
cv.destroyAllWindows()