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

start = 1
end = 35
g = sp.spfa(start, end, d, p, inq, dis, frm, cnt)
