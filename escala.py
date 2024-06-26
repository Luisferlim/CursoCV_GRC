import cv2 as cv

img = cv.imread('Fotos/dogs.jpg')
cv.imshow("doguinhos", img)

def mudaEscala(quadro, escala = 0.75):
    #funciona para imagens, videos e live :D
    Largura = int(quadro.shape[1]  * escala)
    Altura = int(quadro.shape[0] * escala)
    dimensoes = (Largura, Altura)
    return cv.resize(quadro, dimensoes, interpolation = cv.INTER_AREA)

captura = cv.VideoCapture("Videos/cachorrinhofofo.mp4")#0 para mostrar a webcam
# captura = cv.VideoCapture()#0 para mostrar a webcam

while True:
    isTrue, quadro = captura.read()

    novoVideo = mudaEscala(quadro, escala=0.3)
    
    cv.imshow('video', quadro)

    cv.imshow('video novo', novoVideo)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

captura.release()

cv.waitKey(0)
cv.destroyAllWindows()