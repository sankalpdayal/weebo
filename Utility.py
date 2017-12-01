import cv2
import numpy as np
def readLayout(layoutAdd):
	img = cv2.imread(layoutAdd)
	img = cv2.resize(img,(300,300))
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	minLineLength = 10
	maxLineGap = 10
	lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	print('Found',len(lines), 'lines')
	lineSegments = np.array(lines).reshape(len(lines),4)
	print(lineSegments)
	for line in lines:
		x1,y1,x2,y2 = line[0]
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
	cv2.imwrite('houghlines5.jpg',img)
	return img
