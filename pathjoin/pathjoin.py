# Define a abstract data prototype:
class AttributesPairs():
	def __init__(self, pairs):
		self.pairs = pairs

	# sort by the left attributes
	def sortByLeft(self):
		self.pairs.sort(key = lambda x: x[0])

	# sort by the right attributes
	def sortByRight(self):
		self.pairs.sort(key = lambda x: x[1])

	# return an iterator of attributes pairs
	def getPairIterator(self):
		for pair in self.pairs:
			yield pair

	# return a counting dictionary grouped by the left attributes
	def countByLeft(self):
		from collections import Counter
		return dict(Counter(x[0] for x in self.pairs))

	# return a counting dictionary grouped by the right attributes
	def countByRight(self):
		from collections import Counter
		return dict(Counter(x[1] for x in self.pairs))

class ComputePathJoin():
	def __init__(self, pairs_list):
		self.aps_list = [AttributesPairs(pairs) for pairs in pairs_list]

	def computePrelist(self):
		prelist = []
		for i, aps in enumerate(self.aps_list):
			if i == 0:
				prelist.append(aps.countByRight())
			else:
				from collections import defaultdict
				new_pre = defaultdict(int)
				prev_pre = prelist[-1]
				for ap in aps.getPairIterator():
					if ap[0] in prev_pre:
						new_pre[ap[1]] += prev_pre[ap[0]]
				prelist.append(dict(new_pre))
		self.prelist = prelist
		return self.prelist

	def computePostlist(self):
		postlist = []
		for i, aps in enumerate(self.aps_list[::-1]):
			if i == 0:
				postlist.append(aps.countByLeft())
			else:
				from collections import defaultdict
				new_post = defaultdict(int)
				prev_post = postlist[-1]
				for ap in aps.getPairIterator():
					if ap[1] in prev_post:
						new_post[ap[0]] += prev_post[ap[1]]
				postlist.append(dict(new_post))
		postlist.reverse()
		self.postlist = postlist
		return self.postlist

	def computeLocalSensitivity(self):
                print("assert")
                print(self.prelist)
		ls = max(max(self.prelist[-2].values() + [0]), max(self.postlist[1].values()+[0]))
		for i in range(1, len(self.aps_list)-1):
			ls = max(ls, max(self.prelist[i-1].values()+[0]) * max(self.postlist[i+1].values() + [0]))
		self.ls = ls
		return ls

	def solution(self):
		assert(len(self.aps_list) >= 2)
		self.computePrelist()
		self.computePostlist()
		self.computeLocalSensitivity()
		return self.ls

	@classmethod
	def debug(self, sol):
		print 'local sensitivity:', sol.solution()
		print 'prelist:', sol.prelist
		print 'postlist', sol.postlist
		print 'preMax:', [max(x.values()+[0]) for x in sol.prelist]
		print 'postMax:', [max(x.values()+[0]) for x in sol.postlist]
