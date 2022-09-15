import cv2

cap=cv2.VideoCapture(0)
_,img=cap.read()
tracker=cv2.TrackerMedianFlow_create() #not good if there is a rapid moving you can search another trackers
bbox=cv2.selectROI("Tracker",img,False) #to create a window select the area that got interest , tracker window name  false to crop
tracker.init(img,bbox)
img_array=[]
while True:
    _,img=cap.read()
    
    success,bbox=tracker.update(img) #if there is no object it will show that the object is lost
    if success: #if the objext is detected
        (x,y,w,h)=bbox
        cv2.putText(img,"Status: Working",(40,50),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
        cv2.rectangle(img,(int(x),int(y)),(int(x)+int(w),int(y)+int(h)),(0,0,255),3)
    else:
        cv2.putText(img,"Status: Lost",(40,50),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2) #0.9 is font scale , red   

    cv2.waitKey(1)
    img_array.append(img)
    
    cv2.imshow("img",img)
