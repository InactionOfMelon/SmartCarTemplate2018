class Data:
	def __init__(self, weight):
		self.weight = weight
		self.vertices = {'s': -1, 't': -1, 'u': -1} # starting vertex, ending vertex, current vertex
		self.status = 0 # 0: not started; 1: started; 2: ended; -1: error
