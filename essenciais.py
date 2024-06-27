import cv2 as cv

img = cv.imread('Fotos/ufc.jpg')
cv.imshow('base', img)

#coversao
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cinza', cinza)

#diminuir noise (ruido) 
blur = cv.GaussianBlur(cinza, (3,3), cv.BORDER_DEFAULT)
cv.imshow('suavizacao', blur)

#edge cascade -> deteccao de borda
canny = cv.Canny(blur, 125, 175)
cv.imshow('borda', canny)

#dilating -> dilatar e eroding -> erosao 
dilatado = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dilatacao", dilatado)

#dilating -> dilatar e eroding -> erosao 
erodir = cv.erode(dilatado, (7,7), iterations=3)
cv.imshow("erodido", erodir)

#cortar
corte = img[50:200, 200:400]
cv.imshow('corte', corte)


cv.waitKey(0)
cv.destroyAllWindows()