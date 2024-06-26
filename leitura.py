import cv2 as cv

img = cv.imread('Fotos/dog.webp')

cv.imshow('doguinho', img)

#captura de video

captura = cv.VideoCapture("Videos/cachorrinhofofo.mp4")#0 para mostrar a webcam
# captura = cv.VideoCapture()#0 para mostrar a webcam

while True:
    isTrue, quadro = captura.read()
    cv.imshow('video', quadro)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

captura.release()

cv.waitKey(0)
cv.destroyAllWindows()