import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('/content/margarida.jpg',0)
dimensao = img.shape
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
value = cv2.countNonZero(th1)
titles = ['Original Image', 'Global Thresholding (v = 127)']
images = [img, th1]

for i in range(len(images)):
 plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
 plt.title(titles[i])
 plt.xticks([]),plt.yticks([])
plt.show()
print(dimensao)
print(value)
