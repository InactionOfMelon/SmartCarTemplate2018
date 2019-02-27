import cv2
import numpy as np

def main(img):    
    h,w=img.shape[:2]
    #----------------------------------------------------------------------------
    # trans region from src to dst, (left_bottom,right_bottom,left_top,right_top)
    src_points = np.array([[0., h], [w,h],[0.+190.,0.], [w-190.,0.]], dtype = "float32")
    dst_points = np.array([[0., h], [w,h],[0.,0.], [w,0.]], dtype = "float32")
    #----------------------------------------------------------------------------
    M = cv2.getPerspectiveTransform(src_points,dst_points)

    dst = cv2.warpPerspective(img,M,(w,h)) # (w,h)
    cv2.imwrite('dst.png',dst)
    return dst
    
if __name__ == '__main__':
    img=cv2.imread('5.jpg')
    main(img)
