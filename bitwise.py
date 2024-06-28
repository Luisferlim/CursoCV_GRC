import cv2 as cv
import numpy as np

vazio = np.zeros((400,400), dtype= "uint8")

#retangulo cheio
retangulo = cv.rectangle(vazio.copy(), (30,30), (370,370), 255, -1)

#circulo
circulo = cv.circle(vazio.copy(), (200,200), 200, 255, -1)

cv.imshow("retangulo", retangulo)
cv.imshow("circulo", circulo)

#or = 'ou'
or_ = cv.bitwise_or(retangulo, circulo) 
cv.imshow("or", or_)

#and = 'e'
and_ = cv.bitwise_and(retangulo, circulo)
cv.imshow("and", and_)

#xor = 'ou exclusivo'
xor = cv.bitwise_xor(retangulo, circulo)
cv.imshow("xor", xor)

#not = 'nao'
not_ = cv.bitwise_not(circulo)
cv.imshow("not", not_)

cv.waitKey(0)
cv.destroyAllWindows()