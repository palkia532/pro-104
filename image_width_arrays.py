import numpy as np
import cv2 
#black=np.zeros([600,600])
#print(black)
#black[200:400, 200:400] = 255
#cv2.imshow("blacky",black)

#cv2.waitKey(0)


img = cv2.imread("solar-system.jpg")



text_to_show = "Sun"

#Sun
cv2.putText(img,  
           "Sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=1,  
           color=(255,255,255)
           )
#Mercury
cv2.putText(img,  
           "Mercury",
           (130, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Venus
cv2.putText(img,  
           "Venus",
           (200, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Earth
cv2.putText(img,  
           "Earth",
           (295, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Mars
cv2.putText(img,  
           "Mars",
           (390, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Jupiter
cv2.putText(img,  
           "Jupiter",
           (590, 370),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Saturn
cv2.putText(img,  
           "Saturn",
           (780, 295),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Uranus
cv2.putText(img,  
           "Uranus",
           (980, 290),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
#Neptune
cv2.putText(img,  
           "Neptune",
           (1125, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )

cv2.imshow("output",img)

###### ADDITIONAL ACTIVITY ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)
