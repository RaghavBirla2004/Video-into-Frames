import cv2 as cv


cap = cv.VideoCapture("./video.mp4")
ret,frame = cap.read();
count = 0

while True:
 if ret == True:
    cv.imwrite("./frames/img%d.png"%count, frame)
    cap.set(cv.CAP_PROP_POS_MSEC, 10)
    ret,frame =cap.read()

    cv.imshow("Live Video", frame)
    count += 1

    if cv.waitKey(1) & 0xff == 27:
        break;

cv.destroyAllWindows()
cap.release()


   


