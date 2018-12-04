import cv2
import numpy as np
import time
import kmeans
import trans

def main(img):
  #---------Preprocess

  isShowImage=False

  def showImage(img):
    if isShowImage:
      cv2.imshow("Image",img)
      cv2.waitKey(0)

  h,w=img.shape[:2]

  #if isShowImage:
  #  cv2.namedWindow("Image")

  #---------Detect

  showImage(img)

  dst=trans.main(img)
  showImage(dst)

  gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)
  showImage(gray)

  #-------------------------------------------
  blur_ksize = 19  # Gaussian blur kernel size
  #-------------------------------------------
  
  blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
  showImage(blur_gray)

  canny_lthreshold = 50  # Canny edge detection low threshold
  canny_hthreshold = 150  # Canny edge detection high threshold
  edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
  showImage(edges)

  def roi_mask(img, vertices):
    mask = np.zeros_like(img)
    mask_color = 255
    cv2.fillPoly(mask, vertices, mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img
  #------------------------------------------------------------------
  # region of interest, (left_bottom,left_top,right_top,right_bottom)
  roi_vtx = np.array([[(0, int(h*0.8)), (0, int(h*0.2)), 
                       (w, int(h*0.2)), (w, int(h*0.8))]])
  #------------------------------------------------------------------

  roi_edges = roi_mask(edges, roi_vtx)
  #roi_edges=edges
  showImage(roi_edges)

  rho = 1
  theta = np.pi / 180

  #-------------------------------------------
  threshold = 20 # hough threshold
  #-------------------------------------------

  def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    for line in lines:
      for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)

  def draw_lines_rt(img, lines_rt, color=[0, 255, 0], thickness=2):
    for line in lines_rt:
      for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),color,thickness)

  lines_rt = cv2.HoughLines(roi_edges, rho, theta, threshold)
  index=np.where((lines_rt[:,:,0]<0)[:,0])
  lines_rt[index,:,0]*=-1
  lines_rt[index,:,1]-=np.pi

  '''
  line_img_mid = np.zeros((roi_edges.shape[0], roi_edges.shape[1], 3), dtype=np.uint8)

  draw_lines_rt(line_img_mid,lines_rt)

  showImage(line_img_mid)
  '''

  lines_rt=kmeans.main(lines_rt)
  
  '''
  line_img = np.zeros((roi_edges.shape[0], roi_edges.shape[1], 3), dtype=np.uint8)

  draw_lines_rt(line_img,lines_rt,color=[255, 0, 0])

  showImage(line_img)

  detected=cv2.addWeighted(dst, 0.5, line_img, 1, 0)

  showImage(detected)

  cv2.imwrite('detected.png',detected)
  '''

  #if isShowImage:
  #  cv2.destroyAllWindows()

  print lines_rt

  return lines_rt

if __name__ == '__main__':
  img=cv2.imread('5.jpg')
  start = time.time()
  main(img)
  end = time.time()
  print "time:",end-start


