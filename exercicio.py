import cv2 as cv
import numpy as np

vazio = np.zeros((500,500,3), dtype='uint8')
cv.imshow('vazio', vazio)

vazio[:] = 255,255,255
cv.imshow('vazio branco', vazio)

#bgr
cv.circle(vazio, (255,255), 40, (0,0,255), -1)
cv.imshow('japao', vazio)

cv.waitKey(0)
cv.destroyAllWindows()