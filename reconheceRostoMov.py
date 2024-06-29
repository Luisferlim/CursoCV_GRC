import cv2 as cv

haar_cascade = 'haar_face.xml'

cap = cv.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    sucesso, img = cap.read()

    facecascade = cv.CascadeClassifier(haar_cascade)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face = facecascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in face:
        cv.rectangle(img=img, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,255), thickness=3)
        cv.putText(img, 'Luis', (x,y-1), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
    
    cv.imshow('face', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey()
cv.destroyAllWindows