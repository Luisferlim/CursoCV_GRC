import cv2 as cv

img = cv.imread('Fotos/ufc.jpg')
cv.imshow("ufc", img)

#media simples
media = cv.blur(img,(3,3))
cv.imshow("media", media)

#gaussiana melhor - mais esforco computacional
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gauss", gauss)

#mediana muito bom em reduzir ruido (plastico)
mediana = cv.medianBlur(img, 7)
cv.imshow("mediana", mediana)

#bilateral muito bom para identificar bordas
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)


#brincadeirinhas do luis

# mediaCanny = cv.Canny(media, 125, 175)
# gaussCanny = cv.Canny(gauss, 125, 175)
# medianaCanny = cv.Canny(mediana, 125, 175)
# biCanny = cv.Canny(bilateral, 125, 175)

# cv.imshow('av_canny', averageCanny)
# cv.imshow('ga_canny', gaussCanny)
# cv.imshow('me_canny', medianCanny)
# cv.imshow('bi_canny', biCanny)

#fazendo o canny em todas as suavizacoes que a gente fez
#bitwise fica para a prox aula

cv.waitKey(0)
cv.destroyAllWindows()