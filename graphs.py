
class Node:
	def __init__(self, value, next):
		self.name = value
		self.next = next


'''
	Tell whether we can reach dest from orig
'''
def can_reach(orig, dest):
	if dest is orig:
		return True

	if orig == None:
		return False

	return can_reach(orig.next, dest)


'''
	a ----> b ----> d ---> e
			        ^
 			      	|	
			     	|	
			    	c	

	a -> e: True
	a -> c: False
	c -> e: True
'''

a = Node("a", None)
b = Node("b", None)
c = Node("c", None)
d = Node("d", None)
e = Node("e", None)

a.next = b
b.next = d
d.next = e
c.next = d

print "a to e: " + str(can_reach(a, e))
print "a to c: " + str(can_reach(a, c))
print "c to e: " + str(can_reach(c, e))
