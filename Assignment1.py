# Assignment 1 - Blind and Informed Search
from collections import deque
import itertools

class Node:

	def __init__(self, nodeLetter, gDistance):
		self.letter = nodeLetter
		self.distance = gDistance
		self.children = []
		self.parent = None
	
	def getDistance(self):
		return self.distance

	def getChildren(self):
		return self.children

	def getLetter(self):
		return self.letter

	def getParent(self):
		return self.parent

	def setParent(self, node):
		self.parent = node

	def sortChildren(self):
		self.children.sort

	def addChild(self, node):
		self.children.append(node)

	def addChildren(self, nodes):
		self.children = nodes

class Net:

	def __init__(self):
		self.nodes = {}
		visited = []
		root = None

	def addNode(self, node):
		self.nodes[node.getLetter()] = node

	def setRootByKey(self, key):
		self.root = self.nodes[key]

	def getRoot(self):
		return self.root

	def exampleNet(self):
		s, a, b, c, d, e, f, g = None, None, None, None, None, None, None, None
		s = Node('S', 11.0)
		a = Node('A', 10.4)
		b = Node('B', 6.7)
		c = Node('C', 4.0)
		d = Node('D', 8.9)
		e = Node('E', 6.9)
		f = Node('F', 3.0)
		g = Node('G', 0.0)
		nodeList = [s,a,b,c,d,e,f,g]
		children = {'S' : [a, d], 'A' : [s, d, f], 'B' : [c, e], 'C' : [b, f, g], 'D' : [a, e, s], 'E' : [b, d, f], 'F' : [a, c, e], 'G' : [c]}
		for n in nodeList:
			n.addChildren(children[n.getLetter()])
			self.addNode(n)
			n.sortChildren()
		self.setRootByKey('S')

class BreadthFirst:

	def __init__(self, net, root):
		self.graph = net
		self.root = root
		self.queue = deque()
		self.queue.append(self.root)
		self.visited = []

	def traverse(self):
		while(len(self.queue) != 0.0):
			current = self.queue.popleft()
			self.visited.append(current)
			if(current.getDistance() == 0.0):
				path = deque()
				while(current != None):
					path.appendleft(current.getLetter())
					current = current.parent
				return list(path)
			for child in current.children:
				if(child not in self.visited):
					self.queue.append(child)
					child.setParent(current)

class DepthFirst:
	
	def __init__(self, net, root):
		self.graph = net
		self.root = root
		self.visited = []

	def traverse(self):
		current = self.search(self.root)
		path = deque()
		while(current != None):
			path.appendleft(current.getLetter())
			current = current.getParent()		
		return path

	def search(self, node):
		if(node):
			self.visited.append(node)
			if(node.getDistance() == 0):
				return node
			for n in node.getChildren():
				if(n not in self.visited):
					n.setParent(node)
					return self.search(n)
			return self.search(node.getParent())

class BestFirst:
	def __init__(self, net, root):
		self.graph = net
		self.root = root
		self.visited = []

	def traverse(self):
		current = self.root
		path = deque()
		while(current.getDistance() != 0):
			path.append(current.getLetter())
			self.visited.append(current)
			for a, b in itertools.combinations(current.getChildren(), 2):
				if(a.getDistance() < b.getDistance() and a not in self.visited):
					a.setParent(current)
					current = a
				elif(b not in self.visited):
					b.setParent(current)
					current = b
		path.append(current.getLetter())
		return path

net = Net()
net.exampleNet()
bdf = BreadthFirst(net, net.getRoot())
print("Breadth First: " + str(bdf.traverse()))
dfs = DepthFirst(net, net.getRoot())
print("Depth First: " + str(dfs.traverse()))
bestfs = BestFirst(net, net.getRoot())
print("Best First: " + str(bestfs.traverse()))





		

