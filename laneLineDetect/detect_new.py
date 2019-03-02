import numpy as np
import math
import cv2
import time
import trans

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

def det(vec1, vec2):
	x1, y1 = vec1
	x2, y2 = vec2
	return x1 * y2 - x2 * y1

def len2(vec):
	return vec[0] ** 2 + vec[1] ** 2

def dist2(point1, point2):
	return len2((point1[0] - point2[0], point1[1] - point2[1]))

def dist1(point, line):
	x0, y0 = point
	x1, y1, x2, y2 = line[0]
	return abs(det((x1 - x0, y1 - y0), (x2 - x0, y2 - y0))) / 2 / math.sqrt(len2((x1 - x2, y1 - y2)))

def arg(line):
	x1, y1, x2, y2 = line[0]
	a = math.atan2(float(y2 - y1), float(x2 - x1))
	if a < 0:
		a += np.pi
	return a

def is_same_line(line1, line2):
	#--------------------
	arg_threshold = np.pi * 10 / 180
	dist1_threshold = 16
	#--------------------
	a1 = arg(line1)
	a2 = arg(line2)
	if abs(a1 - a2) > arg_threshold:
		return False
	x11, y11, x12, y12 = line1[0]
	x21, y21, x22, y22 = line2[0]
	d1 = max(dist1((x11, y11), line2), dist1((x12, y12), line2), dist1((x21, y21), line1), dist1((x22, y22), line1))
	if d1 > dist1_threshold:
		return False
	return True

def choose_lines(lines, center_point):
	d_min, l = dist2((-1, -1), center_point), None
	for line in lines:
		x1, y1, x2, y2 = line[0]
		d = min(dist2((x1, y1), center_point), dist2((x2, y2), center_point))
		if d < d_min:
			d_min, l = d, line
	if l is None:
		raise Exception('could not choose lines')
	ls = []
	for line in lines:
		x1, y1, x2, y2 = line[0]
		if is_same_line(line, l):
			ls.append(line)
	return ls
'''
def clean_lines(lines, threshold):
	slope = [[math.atan2(float(y2 - y1),float(x2 - x1)) if (math.atan2(float(y2 - y1),float(x2 - x1))>0)
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
			break
'''

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
			if (abs(slope)<np.pi / 4):
				continue
			#if (abs(k)<horizon_threshold):
			#	continue
			if midx<img.shape[1]/2:
				left_lines.append(line)
			else:
				right_lines.append(line)
				
	#if (len(left_lines) <= 0 or len(right_lines) <= 0):
	#	return 0,0,False
	if len(left_lines) == 0 or len(right_lines) == 0:
		return None,None,False
	if len(left_lines)==0:
		left_lines.append(np.array([[0,0,0,h]]))
	if len(right_lines)==0:
		right_lines.append(np.array([[w,0,w,h]]))
	left_lines = choose_lines(left_lines, (w // 2, h))#clean_lines(left_lines, 0.2)
	right_lines = choose_lines(right_lines, ((w + 1) // 2, h))#clean_lines(right_lines, 0.2)
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
	#if isDraw:
		#print(left_vtx[0], left_vtx[1])
		#print(right_vtx[0], right_vtx[1])

	if abs(left_vtx[0][0]-right_vtx[0][0])<=50 and abs(left_vtx[1][0]-right_vtx[1][0])<=50:
			if left_vtx[0][0]<left_vtx[1][0]:
					left_vtx[0]=(0,0)
					left_vtx[1]=(0,h)
			else:
					right_vtx[0]=(w,0)
					right_vtx[1]=(w,h)
	if isDraw:
		#print(left_vtx[0], left_vtx[1])
		#print(right_vtx[0], right_vtx[1])
		cv2.line(img, left_vtx[0], left_vtx[1], [0,0,255], thickness) #Red
		cv2.line(img, right_vtx[0], right_vtx[1], [0,255,0], thickness) #Green
	
	return left_vtx,right_vtx,True

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap,horizon_threshold):
	lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
							minLineLength=min_line_len, maxLineGap=max_line_gap)
	#print(lines)
	line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	lines_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	#draw_lines(line_img, lines)
	draw_lines(lines_img, lines)
	showImage(lines_img)
	lvtx,rvtx,result=draw_lanes(line_img, lines,horizon_threshold)
	if result==False:
		return line_img,lvtx,rvtx,False
	return line_img,lvtx,rvtx,True

def detect_lines(img):
	rate=2
	img=cv2.resize(img,(img.shape[1]//rate,img.shape[0]//rate))
	
	h,w=img.shape[:2]
	showImage(img)
	#import trans
	#img = trans.main(img)
	#showImage(img)

	#--------------
	white_thresh = 235

	blur_ksize = 5 #9  # Gaussian blur kernel size
	canny_lthreshold = 100//rate  # Canny edge detection low threshold
	canny_hthreshold = 200//rate  # Canny edge detection high threshold
	
	# Hough transform parameters
	rho = 1
	theta = np.pi / 180
	threshold = 15//rate
	min_line_length = 60//rate
	max_line_gap = 20//rate
	
	#roi_vtx = np.array([[(0, int(h*0.4)), (0, int(h)),
	#				   (w, int(h)), (w, int(h*0.4))]])
	roi_vtx = np.array([[(0, h), (0, 0), (w, 0), (w, h)]])

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
	
	line_img,leftVtx,rightVtx,isDetected= hough_lines(roi_edges, rho, theta, threshold,
												  min_line_length, max_line_gap,horizon_threshold)
	
	if isDetected==False:
		print('detect failed')
		return 0,False,None,None
	if isDraw:
		res=cv2.addWeighted(img, 1, line_img, 1, 0, img)
		showImage(res)
                
	for i in range(2):
		leftVtx[i]=list(leftVtx[i])
		rightVtx[i]=list(rightVtx[i])
		for j in range(2):
			leftVtx[i][j]*=rate
			rightVtx[i][j]*=rate

	leftX=leftVtx[0][0]
	rightX=rightVtx[0][0]
	leftOffset=w*rate/2-leftX
	rightOffset=rightX-w*rate/2
	offset=rightOffset-leftOffset

	print('detect success')
	#last_error=offset
	return offset,True,leftVtx,rightVtx

def detect_point(img, t = 0, lines = None): # t: current time
	#---------Parameters
	#-------------------------------------------
	PYR_TIMES = 2 # Times of pyrDown()
	PYR_SCALE = 2 ** PYR_TIMES
	HSV_H_MIN, HSV_H_MAX = 5, 27 # H range of red # 5, 13 # 5, 16
	HSV_S_MIN, HSV_S_MAX = 43, 255 # S range of red # 65, 255
	HSV_V_MIN, HSV_V_MAX = 160, 255 # V range of red # 46, 255
	BOX_KSIZE_W_RADIUS = int(50 / PYR_SCALE)  # Kernal width radius of boxFilter
	BOX_KSIZE_W = BOX_KSIZE_W_RADIUS * 2 + 1
	BOX_KSIZE_H_RADIUS = int(45 / PYR_SCALE)  # Kernal height radius of boxFilter
	BOX_KSIZE_H = BOX_KSIZE_H_RADIUS * 2 + 1
	BOX_THRESHOLD = 0.4 # Threshold of boxFilter result
	CENTER_THRESHOLD_RATIO_MAX = 1
	CENTER_THRESHOLD_RATIO_MIN = 0.3
	CENTER_THRESHOLD_RATIO_WIDTH = CENTER_THRESHOLD_RATIO_MAX - CENTER_THRESHOLD_RATIO_MIN
	STARTUP_TIME = 0.5
	STARTUP_TIME_HALF = float(STARTUP_TIME) / 2
	#-------------------------------------------
	#---------Resizes
	small = img.copy()
	for i in range(PYR_TIMES):
		small = cv2.pyrDown(small)
	showImage(small)
	h,w=small.shape[:2]
	#---------Converts to HSV
	hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
	showImage(hsv)
	#---------Detects color
	___, dst = cv2.threshold(cv2.inRange(hsv, np.array([HSV_H_MIN, HSV_S_MIN, HSV_V_MIN]), np.array([HSV_H_MAX, HSV_S_MAX, HSV_V_MAX])), 0, 255, cv2.THRESH_BINARY)
	showImage(dst)
	dst.astype(np.int16)
	#---------Finds point within road
	#print lines
	#print "lines not none"
	#x1, y1, x2, y2 = lines[0][0]
	if lines is None:
		lines = [None, None]
	if lines[0] is not None:
		x1,y1=lines[0][0]
		x2,y2=lines[0][1]
		#print x1,y1,x2,y2
		if y1 > y2:
			x1, y1, x2, y2 = x2, y2, x1, y1
		top_left = x1 / PYR_SCALE
		bottom_left = x2 / PYR_SCALE
	else:
		top_left = bottom_left = w * (1 / 4)
	if lines[1] is not None:
		#x1, y1, x2, y2 = lines[1][0]
		x1,y1=lines[1][0]
		x2,y2=lines[1][1]
		#print x1,y1,x2,y2
		if y1 > y2:
			x1, y1, x2, y2 = x2, y2, x1, y1
		top_right = x1 / PYR_SCALE
		bottom_right = x2 / PYR_SCALE
	else:
		top_right = bottom_right = w * (3 / 4)
	if lines[0] is not None or lines[1] is not None:
		mask = np.zeros_like(dst)
		mask[:, :] = 255
		mask = trans.transform(mask, top_left, top_right, bottom_left, bottom_right)
		showImage(mask)
		dst = cv2.bitwise_and(dst, mask)
	showImage(dst)
	#---------Filters detected color
	res = cv2.boxFilter(dst, -1, (BOX_KSIZE_W, BOX_KSIZE_H), normalize = True)
	res_max = np.max(res)
	if res_max < 255 * BOX_THRESHOLD:
		return None
	else:
		pos = np.where(res == res_max)
		vec = np.sum(pos, axis = 1)
		num = np.size(pos, axis = 1)
		x, y = int(round(float(vec[1]) / num * PYR_SCALE)), int(round(float(vec[0]) / num * PYR_SCALE))
		if isDraw:
			img1 = img.copy()
			draw_point(img1, (x, y))
			showImage(img1)
		h, w = img.shape[:2]
		ratio = CENTER_THRESHOLD_RATIO_MIN + CENTER_THRESHOLD_RATIO_WIDTH / math.exp((t / STARTUP_TIME_HALF - 1) * 3.5)
		return h-y
		return y > h * ratio

if __name__ == '__main__':
	isShowImage=True
	isDraw=True
	start = time.time()
	#last_error=-200
	img=cv2.imread('test2.jpg')
	showImage(img)
	lines = detect_lines(img)[2:]
	print(lines)
	end = time.time()
	print("time:", end - start)
	start = time.time()
	print(detect_point(img, 0,lines))
	end = time.time()
	print("time:", end - start)
