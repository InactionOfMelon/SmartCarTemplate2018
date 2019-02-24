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
        #showImage(mask)
	masked_img = cv2.bitwise_and(img, mask)
	return masked_img

def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
	if isDraw:
		if lines is not None:
			for line in lines:
				for x1, y1, x2, y2 in line:
					cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def draw_point(img, point, k = 127, kmax = 255):
	if isDraw:
		k /= kmax
		cv2.circle(img, point, 3, (int(255 * k), 0, 0), 3)

def clean_lines(lines, threshold):
	arg_max, l = -1, []
	for line in lines:
		x1, y1, x2, y2 = line[0]
		arg = math.atan2(float(y2 - y1), float(x2 - x1))
		if arg < 0:
			arg += np.pi
		#if arg > np.pi:
		#	arg -= np.pi
		if arg > np.pi / 2:
			arg = np.pi - arg
		if arg > arg_max:
			arg_max, l = arg, line
	return [l]
	'''slope = [[math.atan2(float(y2 - y1),float(x2 - x1)) if (math.atan2(float(y2 - y1),float(x2 - x1))>0)
			  else math.atan2(float(y2 - y1),float(x2 - x1))+np.pi,
			  abs(x2*y1-x1*y2)/np.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))]
			 for line in lines for x1, y1, x2, y2 in line]
	#print(slope)
	norm=np.max(np.abs(slope),axis=0)
	slope=list(slope/norm)
	#print(slope)
	while len(lines) > 0:
		mean = np.mean(slope,axis=0)
		diff = [np.sqrt(sum(pow(s - mean,2))) for s in slope]
		idx = np.argmax(diff)
		if diff[idx] > threshold:
			slope.pop(idx)
			lines.pop(idx)
		else:
			break'''

def calc_lane_vertices(point_list, ymin, ymax, img):
	#------------------------
	'''y_chunks = 5 # number of chunks of height
	y_chunk_size = (ymax - ymin) // y_chunks + 1'''
	#------------------------
	x = [p[0] for p in point_list]
	y = [p[1] for p in point_list]
	'''x, y = [], []
	kmax = (y_chunks + 1) ** 2
	for p in point_list:
		k = ((p[0] - ymin) // y_chunk_size + 1) ** 2
		x += [p[0]] * k
		y += [p[1]] * k
		draw_point(img, p, k, kmax)'''
	fit = np.polyfit(y, x, 1)
	fit_fn = np.poly1d(fit)
	
	xmin = int(fit_fn(ymin))
	xmax = int(fit_fn(ymax))
  
	return [(xmin, ymin), (xmax, ymax)]

#last_error=0

def draw_lanes(img, lines, horizon_threshold,color=[0, 255, 0], thickness=8):
	if lines is None:
		return 0,0,False
	if isDraw:
		draw_lines(img,lines,[255,255,255])
        
	h,w=img.shape[:2]
        
	left_lines, right_lines = [], []
	for line in lines:
		for x1, y1, x2, y2 in line:
			slope=math.atan2(float(y2)-float(y1),float(x2)-float(x1))
			#k = (float(y2) - float(y1)) / (x2 - x1)
			midx=(x1+x2)/2
			if (abs(slope)<np.pi/4):
				continue
			#if (abs(k)<horizon_threshold):
			#	continue
			if midx<img.shape[1]/2:
				left_lines.append(line)
			else:
				right_lines.append(line)
				
	#if (len(left_lines) <= 0 or len(right_lines) <= 0):
	#	return 0,0,False
	if len(left_lines)==0:
		left_lines.append(np.array([[0,0,0,h]]))
	if len(right_lines)==0:
		right_lines.append(np.array([[w,0,w,h]]))
	left_lines = clean_lines(left_lines, 0.2)
	right_lines = clean_lines(right_lines, 0.2)
	left_lines_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	draw_lines(left_lines_img, left_lines)
	showImage(left_lines_img)
	right_lines_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	draw_lines(right_lines_img, right_lines)
	showImage(right_lines_img)
	#print(left_lines)
	#print(right_lines)

	if isDraw:
		draw_lines(img,left_lines,[255,0,0])
		draw_lines(img,right_lines,[0,0,255])
	
	left_points = [(x1, y1) for line in left_lines for x1,y1,x2,y2 in line]
	left_points = left_points + [(x2, y2) for line in left_lines for x1,y1,x2,y2 in line]
	right_points = [(x1, y1) for line in right_lines for x1,y1,x2,y2 in line]
	right_points = right_points + [(x2, y2) for line in right_lines for x1,y1,x2,y2 in line]
  
	left_vtx = calc_lane_vertices(left_points, 0, img.shape[0], img)
	right_vtx = calc_lane_vertices(right_points, 0, img.shape[0], img)
	if isDraw:
		print(left_vtx[0], left_vtx[1])
		print(right_vtx[0], right_vtx[1])

	if abs(left_vtx[0][0]-right_vtx[0][0])<=50 and abs(left_vtx[1][0]-right_vtx[1][0])<=50:
			if left_vtx[0][0]<left_vtx[1][0]:
					left_vtx[0]=(0,0)
					left_vtx[1]=(0,h)
			else:
					right_vtx[0]=(w,0)
					right_vtx[1]=(w,h)
	if isDraw:
		print(left_vtx[0], left_vtx[1])
		print(right_vtx[0], right_vtx[1])
		cv2.line(img, left_vtx[0], left_vtx[1], [0,0,255], thickness) #Red
		cv2.line(img, right_vtx[0], right_vtx[1], [0,255,0], thickness) #Green
	
	return left_vtx[0][0],right_vtx[0][0],True

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap,horizon_threshold):
	lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
							minLineLength=min_line_len, maxLineGap=max_line_gap)
	line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	lines_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	#draw_lines(line_img, lines)
	draw_lines(lines_img, lines)
	showImage(lines_img)
	x1,x2,result=draw_lanes(line_img, lines,horizon_threshold)
	if result==False:
		return line_img,x1,x2,False
	return line_img,x1,x2,True

def detect_lines(img):
	h,w=img.shape[:2]
	showImage(img)

	#--------------
	white_thresh = 225

	blur_ksize = 9  # Gaussian blur kernel size
	canny_lthreshold = 100  # Canny edge detection low threshold
	canny_hthreshold = 200  # Canny edge detection high threshold
	
	# Hough transform parameters
	rho = 1
	theta = np.pi / 180
	threshold = 15
	min_line_length = 40
	max_line_gap = 20
	
	roi_vtx = np.array([[(0, int(h*0.4)), (0, int(h)),
					   (w, int(h)), (w, int(h*0.4))]])
	#roi_vtx = np.array([[(0, h), (0, 0), (w, 0), (w, h)]])

	horizon_threshold=1 # threshold for slope of horizontal lines, maybe should be larger 
	
	#--------------
	
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	showImage(gray)
	_retval, th_gray = cv2.threshold(gray, white_thresh, 0, cv2.THRESH_TOZERO)
	showImage(th_gray)
	blur_gray = cv2.GaussianBlur(th_gray, (blur_ksize, blur_ksize), 0, 0)
	showImage(blur_gray)
	edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
	showImage(edges)
	roi_edges = roi_mask(edges, roi_vtx)
	showImage(roi_edges)
	
	line_img,leftX,rightX,isDetected= hough_lines(roi_edges, rho, theta, threshold,
												  min_line_length, max_line_gap,horizon_threshold)
	
	if isDetected==False:
		print('detect failed')
		return 0,False
	res=cv2.addWeighted(img, 1, line_img, 1, 0, img)
	showImage(res)

	leftOffset=w/2-leftX
	rightOffset=rightX-w/2
	offset=rightOffset-leftOffset

	print('detect success')
	#last_error=offset
	return offset,True

if __name__ == '__main__':
	isShowImage=True
	isDraw=True
	img = cv2.imread('lalala.jpg')
	start = time.time()
	#last_error=-200
	print(detect_lines(img))
	showImage(img)
	end = time.time()
	print("time:", end - start)
  
