import cv2 as cv
import os
import numpy as np

pessoas = ['Anitta', 'Clodovil', 'Luan Santana', 'Matue', 'Ze Felipe']
DIR = r'C:\Users\Luis Win\Desktop\minicurso_materias\Faces\treino'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
legendas = []

def criarTreino():
    for pessoa in pessoas:
        caminho = os.path.join(DIR, pessoa)
        legenda = pessoas.index(pessoa)

        for img in os.listdir(caminho):
            img_caminho = os.path.join(caminho, img)

            img_array = cv.imread(img_caminho)

            if img_array is None:
                continue

            cinza = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(cinza, 1.1, 4)

            for (x,y,w,h) in faces_rect:
                face_rei = cinza[y:y+h, x:x+w]

                features.append(face_rei)
                legendas.append(legenda)

criarTreino()
print("Trenamento feito! :D")

features = np.array(features, dtype='object')
legenda = np.array(legendas)

reconhecerFace = cv.face.LBPHFaceRecognizer_create()

reconhecerFace.train(features, legenda)

reconhecerFace.save('faces_treino.yml')

np.save('features.npy', features)
np.save('legenda.npy', legenda)
