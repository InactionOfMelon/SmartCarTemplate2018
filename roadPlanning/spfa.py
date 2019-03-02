import math

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def Vector(p1, p2):
	return Point(p2.x - p1.x, p2.y - p1.y)

def Dot(v1, v2):
	return v1.x * v2.x + v1.y * v2.y

def Cross(v1, v2):
	return v1.x * v2.y - v2.x * v1.y
	
def rotate(v1,v2):
	deg = math.atan2(v2.y, v2.x) - math.atan2(v1.y, v1.x)
	
	while deg > math.pi:
		deg -= math.pi * 2
	while deg < -math.pi:
		deg += math.pi * 2
		
	return deg
	
#calculate the distance between two points
def Length(v):
	return math.sqrt(Dot(v, v))

#calculate the rotate angle
#the return value is positive when turn left
def Angle(p1, p2, p3):
	v1 = Vector(p2, p1)
	v2 = Vector(p3, p2)
	
	if Length(v1) == 0 or Length(v2) == 0:
		return 0
	
	u = Dot(v1, v2)
	#print(v1.x,v1.y)
	#print(v2.x,v2.y)
	#sn = math.acos(Dot(v2, v1) / Length(v1) / Length(v2))
	
	sn = rotate(v1,v2)
	
	ret = math.degrees(sn) + 0.5
	return math.floor(ret)

#return the rotate angle
def Turn(g, k):
	if k == 0:
		v1 = Point(0, 10) #need to modify
		v2 = Vector(g[0], g[1])
		
		
		#print(g[0].x,g[0].y)
		#print(g[1].x,g[1].y)
		#sn = math.acos(Dot(v2, v1) / Length(v1) / Length(v2))
		
		sn = rotate(v1,v2)
		
		ret = math.degrees(sn) + 0.5
		return math.floor(ret)
	else:
		return Angle(g[k - 1], g[k], g[k + 1])

		
inf = math.pow(2, 30) - 1
#initialize the graph
def init_spfa(d, cnt, frm, inq):
	for i in range(1, 56):
		d[i] = inf
		cnt[i] = inf
		frm[i] = 0
		inq[i] = 0
def init_graph(p, dis):
	for i in range(1, 56):
		for j in range(1, 56):
			dis[i][j] = inf
	for i in range(1, 56):
		dis[i][i] = 0
	p.append(Point(0, 0))
	p.append(Point(150, 150))
	p.append(Point(1150, 150))
	p.append(Point(2550, 150))
	p.append(Point(3200, 150))
	p.append(Point(4300, 150))
	p.append(Point(5850, 150))
	p.append(Point(150, 1000))
	p.append(Point(800, 1000))
	p.append(Point(973, 900))
	p.append(Point(1150, 900))
	p.append(Point(1900, 900))
	p.append(Point(2550, 900))
	p.append(Point(3200, 900))
	p.append(Point(4300, 900))
	p.append(Point(5250, 900))
	p.append(Point(5850, 900))
	p.append(Point(3200, 1550))
	p.append(Point(4300, 1550))
	p.append(Point(5250, 1550))
	p.append(Point(5850, 1550))
	p.append(Point(150, 1950))
	p.append(Point(1150, 1950))
	p.append(Point(1900, 1950))
	p.append(Point(2550, 1950))
	p.append(Point(3200, 2250))
	p.append(Point(4300, 2250))
	p.append(Point(5850, 2250))
	p.append(Point(150, 3250))
	p.append(Point(1150, 3250))
	p.append(Point(1800, 3250))
	p.append(Point(2450, 3250))
	p.append(Point(3200, 3250))
	p.append(Point(4300, 3250))
	p.append(Point(5850, 3250))
	p.append(Point(0, 4100))
	p.append(Point(1800, 4100))
	p.append(Point(2450, 4100))
	p.append(Point(3200, 4100))
	p.append(Point(3750, 4100))
	p.append(Point(4300, 4100))
	p.append(Point(1800, 5500))
	p.append(Point(2450, 5500))
	p.append(Point(2450, 5100))
	p.append(Point(3200, 5100))
	p.append(Point(3550, 4750))
	p.append(Point(3750, 4750))
	p.append(Point(4300, 4750))
	p.append(Point(5850, 4750))
	p.append(Point(4300, 5300))
	p.append(Point(5533, 5300))
	p.append(Point(3200, 5500))
	p.append(Point(3550, 5850))
	p.append(Point(3750, 5850))
	p.append(Point(4300, 5850))
	p.append(Point(5215, 5850))
	dis[1][2] = Length(Vector(p[1], p[2]))
	dis[1][7] = Length(Vector(p[1], p[7]))
	dis[2][1] = Length(Vector(p[2], p[1]))
	dis[2][3] = Length(Vector(p[2], p[3]))
	dis[2][10] = Length(Vector(p[2], p[10]))
	dis[3][2] = Length(Vector(p[3], p[2]))
	dis[3][4] = Length(Vector(p[3], p[4]))
	dis[3][12] = Length(Vector(p[3], p[12]))
	dis[4][3] = Length(Vector(p[4], p[3]))
	dis[4][5] = Length(Vector(p[4], p[5]))
	dis[4][13] = Length(Vector(p[4], p[13]))
	dis[5][4] = Length(Vector(p[5], p[4]))
	dis[5][6] = Length(Vector(p[5], p[6]))
	dis[5][14] = Length(Vector(p[5], p[14]))
	dis[6][5] = Length(Vector(p[6], p[5]))
	dis[6][16] = Length(Vector(p[6], p[16]))
	dis[7][1] = Length(Vector(p[7], p[1]))
	dis[7][8] = Length(Vector(p[7], p[8]))
	dis[7][21] = Length(Vector(p[7], p[21]))
	dis[8][7] = Length(Vector(p[8], p[7]))
	dis[8][9] = Length(Vector(p[8], p[9]))
	dis[9][8] = Length(Vector(p[9], p[8]))
	dis[9][10] = Length(Vector(p[9], p[10]))
	dis[10][2] = Length(Vector(p[10], p[2]))
	dis[10][9] = Length(Vector(p[10], p[9]))
	dis[10][11] = Length(Vector(p[10], p[11]))
	dis[10][22] = Length(Vector(p[10], p[22]))
	dis[11][10] = Length(Vector(p[11], p[10]))
	dis[11][12] = Length(Vector(p[11], p[12]))
	dis[11][23] = Length(Vector(p[11], p[23]))
	dis[12][3] = Length(Vector(p[12], p[3]))
	dis[12][11] = Length(Vector(p[12], p[11]))
	dis[12][13] = Length(Vector(p[12], p[13]))
	dis[12][24] = Length(Vector(p[12], p[24]))
	dis[13][4] = Length(Vector(p[13], p[4]))
	dis[13][12] = Length(Vector(p[13], p[12]))
	dis[13][14] = Length(Vector(p[13], p[14]))
	dis[13][17] = Length(Vector(p[13], p[17]))
	dis[14][5] = Length(Vector(p[14], p[5]))
	dis[14][13] = Length(Vector(p[14], p[13]))
	dis[14][15] = Length(Vector(p[14], p[15]))
	dis[14][18] = Length(Vector(p[14], p[18]))
	dis[15][14] = Length(Vector(p[15], p[14]))
	dis[15][16] = Length(Vector(p[15], p[16]))
	dis[15][19] = Length(Vector(p[15], p[19]))
	dis[16][6] = Length(Vector(p[16], p[6]))
	dis[16][15] = Length(Vector(p[16], p[15]))
	dis[16][20] = Length(Vector(p[16], p[20]))
	dis[17][13] = Length(Vector(p[17], p[13]))
	dis[17][18] = Length(Vector(p[17], p[18]))
	dis[17][25] = Length(Vector(p[17], p[25]))
	dis[18][14] = Length(Vector(p[18], p[14]))
	dis[18][17] = Length(Vector(p[18], p[17]))
	dis[18][19] = Length(Vector(p[18], p[19]))
	dis[18][26] = Length(Vector(p[18], p[26]))
	dis[19][15] = Length(Vector(p[19], p[15]))
	dis[19][18] = Length(Vector(p[19], p[18]))
	dis[19][20] = Length(Vector(p[19], p[20]))
	dis[20][16] = Length(Vector(p[20], p[16]))
	dis[20][19] = Length(Vector(p[20], p[19]))
	dis[20][27] = Length(Vector(p[20], p[27]))
	dis[21][7] = Length(Vector(p[21], p[7]))
	dis[21][22] = Length(Vector(p[21], p[22]))
	dis[21][28] = Length(Vector(p[21], p[28]))
	dis[22][10] = Length(Vector(p[22], p[10]))
	dis[22][21] = Length(Vector(p[22], p[21]))
	dis[22][23] = Length(Vector(p[22], p[23]))
	dis[22][29] = Length(Vector(p[22], p[29]))
	dis[23][11] = Length(Vector(p[23], p[11]))
	dis[23][22] = Length(Vector(p[23], p[22]))
	dis[23][24] = Length(Vector(p[23], p[24]))
	dis[24][12] = Length(Vector(p[24], p[12]))
	dis[24][23] = Length(Vector(p[24], p[23]))
	dis[24][25] = Length(Vector(p[24], p[25]))
	dis[25][17] = Length(Vector(p[25], p[17]))
	dis[25][24] = Length(Vector(p[25], p[24]))
	dis[25][26] = Length(Vector(p[25], p[26]))
	dis[25][32] = Length(Vector(p[25], p[32]))
	dis[26][18] = Length(Vector(p[26], p[18]))
	dis[26][25] = Length(Vector(p[26], p[25]))
	dis[26][27] = Length(Vector(p[26], p[27]))
	dis[26][33] = Length(Vector(p[26], p[33]))
	dis[27][20] = Length(Vector(p[27], p[20]))
	dis[27][26] = Length(Vector(p[27], p[26]))
	dis[27][34] = Length(Vector(p[27], p[34]))
	dis[28][21] = Length(Vector(p[28], p[21]))
	dis[28][29] = Length(Vector(p[28], p[29]))
	dis[29][22] = Length(Vector(p[29], p[22]))
	dis[29][28] = Length(Vector(p[29], p[28]))
	dis[29][30] = Length(Vector(p[29], p[30]))
	dis[30][29] = Length(Vector(p[30], p[29]))
	dis[30][31] = Length(Vector(p[30], p[31]))
	dis[30][36] = Length(Vector(p[30], p[36]))
	dis[31][30] = Length(Vector(p[31], p[30]))
	dis[31][32] = Length(Vector(p[31], p[32]))
	dis[31][37] = Length(Vector(p[31], p[37]))
	dis[32][25] = Length(Vector(p[32], p[25]))
	dis[32][31] = Length(Vector(p[32], p[31]))
	dis[32][33] = Length(Vector(p[32], p[33]))
	dis[32][38] = Length(Vector(p[32], p[38]))
	dis[33][26] = Length(Vector(p[33], p[26]))
	dis[33][32] = Length(Vector(p[33], p[32]))
	dis[33][34] = Length(Vector(p[33], p[34]))
	dis[33][40] = Length(Vector(p[33], p[40]))
	dis[34][27] = Length(Vector(p[34], p[27]))
	dis[34][33] = Length(Vector(p[34], p[33]))
	dis[34][48] = Length(Vector(p[34], p[48]))
	dis[35][36] = Length(Vector(p[35], p[36]))
	dis[36][30] = Length(Vector(p[36], p[30]))
	dis[36][35] = Length(Vector(p[36], p[35]))
	dis[36][37] = Length(Vector(p[36], p[37]))
	dis[36][41] = Length(Vector(p[36], p[41]))
	dis[37][31] = Length(Vector(p[37], p[31]))
	dis[37][36] = Length(Vector(p[37], p[36]))
	dis[37][38] = Length(Vector(p[37], p[38]))
	dis[38][32] = Length(Vector(p[38], p[32]))
	dis[38][37] = Length(Vector(p[38], p[37]))
	dis[38][39] = Length(Vector(p[38], p[39]))
	dis[38][44] = Length(Vector(p[38], p[44]))
	dis[39][38] = Length(Vector(p[39], p[38]))
	dis[39][40] = Length(Vector(p[39], p[40]))
	dis[39][46] = Length(Vector(p[39], p[46]))
	dis[40][33] = Length(Vector(p[40], p[33]))
	dis[40][39] = Length(Vector(p[40], p[39]))
	dis[40][47] = Length(Vector(p[40], p[47]))
	dis[41][36] = Length(Vector(p[41], p[36]))
	dis[41][42] = Length(Vector(p[41], p[42]))
	dis[42][41] = Length(Vector(p[42], p[41]))
	dis[42][43] = Length(Vector(p[42], p[43]))
	dis[43][42] = Length(Vector(p[43], p[42]))
	dis[43][44] = Length(Vector(p[43], p[44]))
	dis[44][38] = Length(Vector(p[44], p[38]))
	dis[44][43] = Length(Vector(p[44], p[43]))
	dis[44][45] = Length(Vector(p[44], p[45]))
	dis[44][51] = Length(Vector(p[44], p[51]))
	dis[45][44] = Length(Vector(p[45], p[44]))
	dis[45][46] = Length(Vector(p[45], p[46]))
	dis[46][39] = Length(Vector(p[46], p[39]))
	dis[46][45] = Length(Vector(p[46], p[45]))
	dis[46][47] = Length(Vector(p[46], p[47]))
	dis[46][53] = Length(Vector(p[46], p[53]))
	dis[47][40] = Length(Vector(p[47], p[40]))
	dis[47][46] = Length(Vector(p[47], p[46]))
	dis[47][48] = Length(Vector(p[47], p[48]))
	dis[47][49] = Length(Vector(p[47], p[49]))
	dis[48][34] = Length(Vector(p[48], p[34]))
	dis[48][47] = Length(Vector(p[48], p[47]))
	dis[48][50] = Length(Vector(p[48], p[50]))
	dis[49][47] = Length(Vector(p[49], p[47]))
	dis[49][50] = Length(Vector(p[49], p[50]))
	dis[49][54] = Length(Vector(p[49], p[54]))
	dis[50][48] = Length(Vector(p[50], p[48]))
	dis[50][49] = Length(Vector(p[50], p[49]))
	dis[50][55] = Length(Vector(p[50], p[55]))
	dis[51][44] = Length(Vector(p[51], p[44]))
	dis[51][52] = Length(Vector(p[51], p[52]))
	dis[52][51] = Length(Vector(p[52], p[51]))
	dis[52][53] = Length(Vector(p[52], p[53]))
	dis[53][46] = Length(Vector(p[53], p[46]))
	dis[53][52] = Length(Vector(p[53], p[52]))
	dis[53][54] = Length(Vector(p[53], p[54]))
	dis[54][49] = Length(Vector(p[54], p[49]))
	dis[54][53] = Length(Vector(p[54], p[53]))
	dis[54][55] = Length(Vector(p[54], p[55]))
	dis[55][50] = Length(Vector(p[55], p[50]))
	dis[55][54] = Length(Vector(p[55], p[54]))



#return a list that contain the shortest path
def spfa(start, end, d, p, inq, dis, frm, cnt):
	q = []
	head = -1
	tail = 0
	q.append(start)
	inq[start] = 1
	cnt[start] = 0
	d[start] = 0
	frm[start] = start
	inf = math.pow(2, 30) - 1

	while head < tail:
		head = head + 1
		k = q[head]
		for i in range(1, 56):
			if dis[k][i] == inf:
				continue
			w = 0
			u = Angle(p[frm[k]], p[k], p[i])
			if math.fabs(u) > 0:
				w = 1
			if (cnt[k] + w < cnt[i]) or (cnt[k] + w == cnt[i] and d[k] + dis[k][i] < d[i]):
				cnt[i] = cnt[k] + w
				d[i] = d[k] + dis[k][i]
				frm[i] = k
				if inq[i] == 0:
					inq[i] = 1
					tail = tail + 1
					q.append(i)

	ret = []
	pos = end
	while True:
		ret.append(pos)
		if pos == start:
			break
		pos = frm[pos]
	ret.reverse()
	return ret
