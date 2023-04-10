import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    try:

        laplacian = cv2.Laplacian(frame,cv2.CV_64F)
        laplacian = np.uint8(laplacian)

        edges = cv2.Canny(frame,150,150)
        _,mask = cv2.threshold(edges,254,255,cv2.THRESH_BINARY)
        contours,_ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            cv2.drawContours(frame,[cnt],-1,(0,0,255),-1)

    except:
        pass

    cv2.imshow("frame",frame)
    # cv2.imshow("laplacian",laplacian)
    # cv2.imshow("edges",edges)

    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()
    