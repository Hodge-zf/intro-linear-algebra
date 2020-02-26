class Vec:
	def __init__(self, labels, function):
		self.D = labels
		self.f = function

	def zero_vec(D): 
		return Vec(D, {d:0 for d in D})

	def setitem(v, d, val):
		v.f[d] = val

	def getitem(v,d):
		if d in v.d:
			return v.f[d]
		else:
			return 0
