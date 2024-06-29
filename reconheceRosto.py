import cv2 as cv

face = cv.imread('Fotos/grupo 2.webp')
cv.imshow('face', face)

face_cinza = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
cv.imshow('face cinza', face_cinza)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rec = haar_cascade.detectMultiScale(face_cinza, 1.1, minNeighbors=4)

print(f'Numero de faces encontradas = {len(face_rec)}')

for (x,y,w,h) in face_rec:
    cv.rectangle(face, (x,y), (x+ w, y+ h), (0,0,255), thickness=2)

cv.imshow('detectado', face)

cv.waitKey(0)
cv.destroyAllWindows()