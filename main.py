import math
import os
import time
import sys
sys.path.append("laneLineDetect/")
sys.path.append("roadPlanning/")
sys.path.append("Pi/")
import car
import straight
import camera
import adjustment
import spfa as sp
from mqtt import MQTT
from data import Data


#initialize the list


car.set_pid_param(3,0,1)

N = 60
p = []
dir = []
dis = [[0 for col in range(N)] for row in range(N)]
d = [0 for i in range(N)]
cnt = [0 for i in range(N)]
frm = [0 for i in range(N)]
inq = [0 for i in range(N)]

sp.init_graph(p, dis, dir)
sp.init_spfa(d, cnt, frm, inq)
data = Data(dis)
mqtt = MQTT(data)
handler = camera.Handler()

def work(start, end):
	not_ended = True
	while not_ended:
		sp.init_spfa(d, cnt, frm, inq)
		R = sp.spfa(start, end, d, p, inq, dis, frm, cnt)
		pos = [sp.Point(p[start].x - dir[start].x, p[start].y - dir[start].y)]
		for i in R:
			#print(i,p[i].x,p[i].y)
			pos.append((p[i], i))
		
		n = len(R)
		count = 0
		
		print('Trip start!')
		print(R)
		Angle = sp.Turn(pos, 1)
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
				Angle = sp.Turn(pos, i+1)
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
			print('current:', 'expecting', R[i], '; actually', data.vertices['u'])
			if data.vertices['u'] != -1 and R[i] != data.vertices['u']:
				not_ended = True
				break
		start = data.vertices['u']

while mqtt.client.not_connected or data.vertices['s'] == -1:
	time.sleep(0)
start = data.vertices['s']#=int(input())
end = data.vertices['t']#=int(input())
while data.status == 0:
	time.sleep(0)
try:
	work(start, end)
except KeyboardInterrupt:
	car.stop()
