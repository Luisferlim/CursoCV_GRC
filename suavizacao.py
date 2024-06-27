import cv2 as cv

img = cv.imread('Fotos/ufc.jpg')
cv.imshow("ufc", img)

#media simples
media = cv.blur(img,(7,7))
cv.imshow("media", media)

#gaussiana melhor - mais esforco computacional
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("gauss", gauss)

#mediana muito bom em reduzir ruido (plastico)
mediana = cv.medianBlur(img, 7)
cv.imshow("mediana", mediana)

#bilateral muito bom para identificar bordas
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)



cv.waitKey(0)
cv.destroyAllWindows()