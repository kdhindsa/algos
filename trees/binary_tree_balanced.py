
class Node:
	def __init__(self, left, right, name):
		self.left = left
		self.right = right
		self.name = name


'''
	Returns the depth of the tree

	node: Node object
	d: depth (int)
'''
def depth(node, d):
	if node == None:
		return d

	if node.left == None and node.right == None:
		return d + 1

	return max(depth(node.left, d + 1), depth(node.right, d + 1))

'''
	Check to see if binary tree is balanced
'''
def isBalanced(node):

	if node == None:
		return true

	diff = abs(depth(node.left, 0) - depth(node.right, 0))
	
	if diff >= 1:
		return false
	
	return isBalanced(node.left) && isBalanced(node.right)

'''
					A
				  /   \
			 	 B     E
			    / \   /
			   C   D F
					  \
					   G
					  /
					 H
'''


a = Node(None, None, "A")
b = Node(None, None, "B")
c = Node(None, None, "C")
d = Node(None, None, "D")
e = Node(None, None, "E")
f = Node(None, None, "F")
g = Node(None, None, "G")
h = Node(None, None, "H")

a.left = b
a.right = e

b.left = c
b.right = d

e.left = f

f.right = g

g.left = h


print isBalanced(a)

g.left = None	# make it balanced
print isBalanced(a)
