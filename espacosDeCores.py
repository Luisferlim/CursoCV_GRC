import cv2 as cv
import matplotlib.pyplot as plt

#BGR
img = cv.imread("Fotos/dogs.jpg")
cv.imshow("dogs", img)

#RGB
# plt.imshow(img)
# plt.show()

#escala de cinza
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("cinza", cinza)

#bgr para HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

#bgr para L * A * B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

#bgr para rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

#cinza para bgr
cinza_bgr = cv.cvtColor(cinza, cv.COLOR_GRAY2BGR)
cv.imshow('cinza bgr', cinza_bgr)

# #exercicio 2
# print(cinza.shape)

# print(hsv.shape)

# print(lab.shape)

cv.waitKey(0)
cv.destroyAllWindows()