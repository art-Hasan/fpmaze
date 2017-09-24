# queue/deque.py

from .deque import Deque

""" Simple queue implementation """
class Queue(Deque):
	def __init__(self):
		Deque.__init__(self)

	# add item to end of queue
	def enqueue(self, data):
		self.add_rear(data)

	# remove item from end of queue
	def dequeue(self):
		return self.remove_front()
