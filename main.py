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
from .Pi.mqtt import MQTT
from .Pi.data import Data


#initialize the list


N = 60
p = []
dis = [[0 for col in range(N)] for row in range(N)]
d = [0 for i in range(N)]
cnt = [0 for i in range(N)]
frm = [0 for i in range(N)]
inq = [0 for i in range(N)]

sp.init_graph(p, dis)
sp.init_spfa(d, cnt, frm, inq)
data = Data(dis)
mqtt = MQTT(data)
handler = camera.Handler()

def work(start, end):
	not_ended = True
	while not_ended:
		sp.init_spfa(d, cnt, frm, inq)
		R = sp.spfa(start, end, d, p, inq, dis, frm, cnt)
		pos = []
		for i in range(len(R)):
			pos.append(p[i])
		
		n = len(R)
		count = 0
		
		print('Trip start!')
		#print(R)
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
				not_ended = False
			else:
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
			print('current:', 'expecting', pos[i], '; actually', data.vertices['u'])
			if pos[i] != data.vertices['u']:
				not_ended = True
				break
		start = data.vertices['u']

if __name__ == '__main__':
	start = data.vertices['s']#int(input())
	end = data.vertices['t']#int(input())
	try:
		work(start, end)
	except KeyboardInterrupt:
		car.stop()
