
import cv2, numpy as np, imutils

cap = cv2.VideoCapture("rtsp://admin:admin@123@192.168.1.2:554/h265/main/ch2/main/av_stream")
writer = None
gray_list = []


while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width = 640)
    (h, w) = frame.shape[:2]
    
    x = frame[89:332,317:401]
    cv2.rectangle(frame,(317,89),(401,332),(255,0,0),5)
    avg_color_per_row = np.average(x, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    #print("first",avg_color)
    
    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    avg_gray_per_row = np.average(gray, axis=0)
    avg_gray = np.average(avg_gray_per_row, axis=0)
    print("first",avg_gray)

    

    gray_list.append(avg_gray)
    if len(gray_list) == 720:
        gray_list.pop(0)
    #print (gray_list)
    if (avg_gray > 74):
        for i in gray_list:
            if i > 74:
                cv2.putText(frame, 'electrical_panels_open', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    
       
    #me, 'electrical_panels_open', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Application", frame)
    
    
    
    
#    cv2.imshow("Application", gray[0:100, 0:100])
    key = cv2.waitKey(1)
    if key == ord ('q'):
        break
cv2.destroyAllWindows()
writer.release()




