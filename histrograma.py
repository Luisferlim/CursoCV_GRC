import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('Fotos/ufcpici.png')
cv.imshow("seara", img)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("cinza", cinza)

vazio = np.zeros(img.shape[:2], dtype='uint8')

mascara = cv.circle(vazio.copy(), (img.shape[1]//2, img.shape[0]//2 + -80), 100, 255, -1)
mascarado = cv.bitwise_and(img, img, mask=mascara)
cv.imshow("mascarado", mascarado)

#histograma cinza
hist_cinza = cv.calcHist([cinza], [0], mascara, [256], [0, 256])

# plt.figure()
# plt.grid()
# plt.title('Histograma cinza')
# plt.xlabel('intensadidade')
# plt.ylabel('numero de pixels')
# plt.plot(hist_cinza)
# plt.xlim([0,256])
# plt.show()

cores = ('b', 'g', 'r')

plt.figure()
plt.grid()
plt.title('Histograma colorido')
plt.xlabel('intensadidade')
plt.ylabel('numero de pixels')


for i, col in enumerate(cores):
    hist = cv.calcHist([img], [i], mascara, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()

