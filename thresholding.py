import cv2 as cv

#thresholding -> limiarizacao/limiar/limite

img = cv.imread('fotos/ufcpici.png')
cv.imshow('ufc', img)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("cinza", cinza)

#limiarizacao simples
threshold, thresh = cv.threshold(cinza, 150, 255, cv.THRESH_BINARY)
cv.imshow("limiar", thresh)

print(threshold)

threshold, thresh_inv = cv.threshold(cinza, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("limiar inverso", thresh_inv)

#adaptave threshold
thresh_adaptativo = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('adaptativo1', thresh_adaptativo)

thresh_adaptativo2 = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 11)
cv.imshow('adaptativo2', thresh_adaptativo2)

thresh_adaptativo3 = cv.adaptiveThreshold(cinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 15)
cv.imshow('adaptativo3', thresh_adaptativo3)


cv.waitKey(0)
cv.destroyAllWindows()