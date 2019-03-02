import spfa as sp

def road_ask(start, end):
	g = sp.spfa(start, end, d, p, inq, dis, frm, cnt)
	return g