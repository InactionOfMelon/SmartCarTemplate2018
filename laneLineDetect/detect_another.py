import numpy as np
import math
import cv2
import time

isShowImage=False
isDraw=False
def showImage(img,winName="Image"):
	if isShowImage:
		cv2.imshow(winName,img)
		cv2.waitKey(0)

def roi_mask(img, vertices):
	mask = np.zeros_like(img)
	mask_color = 255
	cv2.fillPoly(mask, vertices, mask_color)
	masked_img = cv2.bitwise_and(img, mask)
	return masked_img

def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def clean_lines(lines, threshold,last_angle):
        linepair=[]
        for line in lines:
                for x1, y1, x2, y2 in line:
                        if y2>=y1:
                                slope=math.atan2(float(y2 - y1),float(x2 - x1))
                        else:
                                slope=math.atan2(float(y1 - y2),float(x1 - x2))
                        if abs(slope-np.pi-last_angle)<abs(slope-last_angle):
                                slope-=np.pi
                        if abs(slope+np.pi-last_angle)<abs(slope-last_angle):
                                slope+=np.pi
                        dist=abs(x2*y1-x1*y2)/np.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
                        linepair.append([slope,dist])
	#print lines
        #print linepair
	norm=np.max(np.abs(linepair),axis=0)
	linepair=list(linepair/norm)
	#print linepair
	while len(lines) > 0:
		mean = np.mean(linepair,axis=0)
		diff = [np.sqrt(sum(pow(s - mean,2))) for s in linepair]
		idx = np.argmax(diff)
		if diff[idx] > threshold:
			linepair.pop(idx)
			lines.pop(idx)
		else:
			break

def calc_lane_vertices(point_list, ymin, ymax):
	x = [p[0] for p in point_list]
	y = [p[1] for p in point_list]
	fit = np.polyfit(y, x, 1)
	fit_fn = np.poly1d(fit)
	
	xmin = int(fit_fn(ymin))
	xmax = int(fit_fn(ymax))
  
	return [(xmin, ymin), (xmax, ymax)]
def cross(a,b):
        return a[0]*b[1]-b[0]*a[1]
def draw_lanes(img, lines, last_angle,angle_threshold=np.pi/8,color=[0, 255, 0], thickness=8):
        #print lines
	if lines is None:
		return 0,0,False
	if isDraw:
		draw_lines(img,lines,[0,255,255])
        
        select_lines=[]
	left_lines, right_lines = [], []
	for line in lines:
		for x1, y1, x2, y2 in line:
                        if y2<y1:
			        slope=math.atan2(y1-y2,x2-x1)
                        else:
                                slope=math.atan2(y2-y1,x1-x2)
                        #print slope/np.pi
			if abs(slope-last_angle)>angle_threshold and abs(slope-last_angle-np.pi)>angle_threshold and abs(slope-last_angle+np.pi)>angle_threshold:
				continue
                        select_lines.append(line)
        if isDraw:
		draw_lines(img,select_lines,[255,255,0])
        #print select_lines
        globalMid=np.mean([[(x1+x2)/2.0,(y1+y2)/2.0] for line in select_lines for x1,y1,x2,y2 in line],axis=0)
        #print globalMid
        if isDraw:
                cv2.circle(img,(int(globalMid[0]),int(globalMid[1])),20,(0,0,255),-1)
        for line in select_lines:
                for x1,y1,x2,y2 in line:
			midpoint=[(x1+x2)/2.0,(y1+y2)/2.0]
			if cross(midpoint-globalMid,[math.cos(last_angle)*100.0,-math.sin(last_angle)*100.0])>=0:
				left_lines.append(line)
			else:
				right_lines.append(line)
        #print left_lines
        #print right_lines
	if (len(left_lines) <= 0 or len(right_lines) <= 0):
		return 0,0,False
				
	#if isDraw:
	#	draw_lines(img,left_lines,[255,0,0])
	#	draw_lines(img,right_lines,[0,0,255])
                
	clean_lines(left_lines, 1.0,last_angle)
	clean_lines(right_lines, 1.0,last_angle)

	if isDraw:
		draw_lines(img,left_lines,[255,0,0])
		draw_lines(img,right_lines,[0,0,255])
	
	left_points = [(x1, y1) for line in left_lines for x1,y1,x2,y2 in line]
	left_points = left_points + [(x2, y2) for line in left_lines for x1,y1,x2,y2 in line]
	right_points = [(x1, y1) for line in right_lines for x1,y1,x2,y2 in line]
	right_points = right_points + [(x2, y2) for line in right_lines for x1,y1,x2,y2 in line]
  
	left_vtx = calc_lane_vertices(left_points, 0, img.shape[0])
	right_vtx = calc_lane_vertices(right_points, 0, img.shape[0])
	
	if isDraw:
               cv2.line(img, left_vtx[0], left_vtx[1], [0,0,255], thickness) #Red
       	       cv2.line(img, right_vtx[0], right_vtx[1], [0,255,0], thickness) #Green
	
	return left_vtx[0][0],right_vtx[0][0],True

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap,last_angle):
	lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
							minLineLength=min_line_len, maxLineGap=max_line_gap)
	line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	#draw_lines(line_img, lines)
	x1,x2,result=draw_lanes(line_img, lines,last_angle)
	if result==False:
		return line_img,x1,x2,False
	return line_img,x1,x2,True

def detect_lines(img,last_angle):
	h,w=img.shape[:2]
	showImage(img)

	#--------------

	blur_ksize = 5  # Gaussian blur kernel size
	canny_lthreshold = 20  # Canny edge detection low threshold
	canny_hthreshold = 180  # Canny edge detection high threshold
	
	# Hough transform parameters
	rho = 1
	theta = np.pi / 180
	threshold = 15
	min_line_length = 40
	max_line_gap = 20
	
	#roi_vtx = np.array([[(0, int(h*0.9)), (0, int(h*0.1)),
	#				   (w, int(h*0.1)), (w, int(h*0.9))]])
	roi_vtx = np.array([[(0, h), (0, 0), (w, 0), (w, h)]])

	horizon_threshold=1 # threshold for slope of horizontal lines, maybe should be larger 
	
	#--------------
	
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	showImage(gray)
	blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
	showImage(blur_gray)
	edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
	showImage(edges)
	roi_edges = roi_mask(edges, roi_vtx)
	showImage(roi_edges)
	
	line_img,leftX,rightX,isDetected= hough_lines(roi_edges, rho, theta, threshold,
												  min_line_length, max_line_gap,last_angle)
	
	if isDetected==False:
		print 'detect failed'
		return 0,False
	res=cv2.addWeighted(img, 0.5, line_img, 1, 0)
	showImage(res)

	leftOffset=w/2-leftX
	rightOffset=rightX-w/2
	offset=rightOffset-leftOffset

	print 'detect success'
	return offset,True

if __name__ == '__main__':
	isShowImage=True
	isDraw=True
	img = cv2.imread('lane4.jpg')
	start = time.time()
	print detect_lines(img,np.pi/4)
	end = time.time()
	print "time:", end - start
  
