import cv2
import numpy as np

def transform(img, top_left, top_right, bottom_left, bottom_right):
	h, w = img.shape[: 2]
	top_left = float(top_left)
	top_right = float(top_right)
	bottom_left = float(bottom_left)
	bottom_right = float(bottom_right)
	src_points = np.array([[0., h], [w,h],[0.,0.], [w,0.]], dtype = "float32")
	dst_points = np.array([[bottom_left, h], [bottom_right,h],[top_left,0.], [top_right,0.]], dtype = "float32")
	M = cv2.getPerspectiveTransform(src_points,dst_points)
	dst = cv2.warpPerspective(img,M,(w,h)) # (w,h)
	return dst

def main(img):
	h,w=img.shape[:2]
	#----------------------------------------------------------------------------
	# trans region from src to dst, (left_bottom,right_bottom,left_top,right_top)
	src_points = np.array([[0., h], [w,h],[0.+180.,0.], [w-150.,0.]], dtype = "float32")
	dst_points = np.array([[0., h], [w,h],[0.,0.], [w,0.]], dtype = "float32")
	d = w * 0.234375
	#src_points = np.array([[0., h], [w,h], [w-d,0.],[0.+d,0.]], dtype = "float32")
	#dst_points = np.array([[0., h], [w,h],[w,0.],[0.,0.]], dtype = "float32")
	#----------------------------------------------------------------------------
	M = cv2.getPerspectiveTransform(src_points,dst_points)

	dst = cv2.warpPerspective(img,M,(w,h)) # (w,h)
	#cv2.imwrite('dst.png',dst)
	return dst
	
if __name__ == '__main__':
	img=cv2.imread('fig21.jpg')
	cv2.imshow("a",img)
	cv2.waitKey(0)
	img=main(img)
	cv2.imshow("a", img)
	cv2.waitKey(0)
