class TopUsers:
	def__init__(self, log, n):
		self.log = log
		self.user_freq = {}
		self.n = n
		self.buffer = []		

	def parse_log(self):
		self.user_freq[user][word] = word_counter
	
	def find_largest_vocab(self):
		for user in self.user_freq:
			self.buffer.append((len(self.user_freq[user])), user)

	def find_max(self):
		self.parse_log()
		self.find_largest_vocab()
		temp = sorted(self.buffer, key=lambda x: x[0])
		for i in range(self.n):
			return temp[i][1]