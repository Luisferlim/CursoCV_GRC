import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

pessoas = ['Anitta', 'Clodovil', 'Luan Santana', 'Matue', 'Ze Felipe']

features = np.load('features.npy', allow_pickle=True)
legenda = np.load('legenda.npy')

reconhecerFace = cv.face.LBPHFaceRecognizer_create()
reconhecerFace.read("faces_treino.yml")

validacao = cv.imread(r'C:\Users\Luis Win\Desktop\minicurso_materias\Faces\validacao\Anitta\5.jfif')
val_cinza = cv.cvtColor(validacao, cv.COLOR_BGR2GRAY)

cv.imshow('validacao', val_cinza)

#deteccao de fato
face_rec = haar_cascade.detectMultiScale(val_cinza, 1.1, 4)
for (x,y,w,h) in face_rec:
    face_ri = val_cinza[y:y+h, x:x+w]
    legenda, confianca = reconhecerFace.predict(face_ri)
    print(f'legenda {pessoas[legenda]} com confianca de  {confianca}')

    cv.putText(validacao, str(pessoas[legenda]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
    cv.rectangle(validacao, (x,y), (x+w, y+h), (0,0,255), 2)

cv.imshow('detectado', validacao)

cv.waitKey(0)
cv.destroyAllWindows()

