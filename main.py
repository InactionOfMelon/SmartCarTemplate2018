import math
import os
import time
import sys
sys.path.append("laneLineDetect/")
sys.path.append("roadPlanning/")
import car
import straight
import camera
import adjustment
import spfa as sp



#initialize the list


p = []
N = 60
cnt = [0 for i in range(N)]
frm = [0 for i in range(N)]
inq = [0 for i in range(N)]
d = [0 for i in range(N)]
dis = [[0 for col in range(N)] for row in range(N)]

sp.init(p, d, dis, cnt)
	
handler = camera.Handler()

def work(start, end):
	R = sp.spfa(start, end, d, p, inq, dis, frm, cnt)
	pos = []
	for i in R:
		pos.append(p[i])
	
	n = len(R)
	count = 0
	
	print('Trip start!')
	print(R)
	Angle = sp.Turn(pos, 0)
	if math.fabs(Angle) > 7:
		print('********Turn',Angle)
		car.turn(Angle)
		print('********Adjustment')
		adjustment.work(handler)
			
	for i in range(1, n):
		if i==n-1:
			print('********straight:',count)
			straight.work(handler, count)
			count=0
			break
			
		Angle = sp.Turn(pos, i)
		if math.fabs(Angle) <= 7:
			count+=1
		else:
			print('********straight:',count)
			straight.work(handler, count)
			count=0
			car.stop()
			time.sleep(0.5)
			
			print('********Turn',Angle)
			car.turn(Angle)
			car.stop()
			time.sleep(0.5)
			
			print('********Adjustment')
			adjustment.work(handler)
			time.sleep(0.5)

if __name__ == '__main__':
	start = int(input())
	end = int(input())
	work(start, end)