class Solution:
	# Write your code here

	stack = []
	queue = []

	def pushCharacter(self, char):
		self.stack.append(char)

	def enqueueCharacter(self, char):
		self.queue.append(char)

	def popCharacter(self):
		return self.stack.pop()

	def dequeueCharacter(self):
		self.queue.reverse()
		dequeueChar = self.queue.pop()
		self.queue.reverse()
		return dequeueChar
