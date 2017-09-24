# queue/deque.py

""" Simple deque implementation """
class Deque(object):

	def __init__(self):
		self.items = []

	def add_rear(self, item):
		self.items.insert(0, item)

	def add_front(self, item):
		self.items.append(item)

	def remove_front(self):
		return self.items.pop()

	def remove_rear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def __repr__(self):
		return " ".join(str(self.items))
