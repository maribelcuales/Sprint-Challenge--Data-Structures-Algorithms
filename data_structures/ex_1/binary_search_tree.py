class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # hasleft = self.left is not None
    # hasright = self.right is not None

    # cb(self.value)    
    # if hasleft:
    #   self.left.depth_first_for_each(cb)
    # if hasright:
    #   self.right.depth_first_for_each(cb)
    # return

    # Recursive 
    # call the cb on the current BST node
    cb(self.value)
    if self.left: # left most branch 
      self.left.depth_first_for_each(cb)  # if there's a left node/child, will execute the cb; once all the left nodes are exhausted, then proceed to check the right     
    if self.right:
      self.right.depth_first_for_each(cb) # if there's a right node/child, will execute the cb
    
    # # Iterative
    # stack = []
    # #append the root node of our BST
    # stack.append(self)
    # # iterate throught the elements in the stack
    # while len(stack):
    #   # pop off the top-most stack element
    #   current_node = stack.pop()
    #   # check to see if this node has a right child
    #   if current_node.right:
    #     stack.append(current_node.left)
    #   # check to see if this node has a left child
    #   if current_node.left:
    #     stack.append(current_node.left)      
    #   # call the callback
    #   cb(current_node.value)


  def breadth_first_for_each(self, cb):    
    # nodes = [self]

    # while len(nodes) > 0:
    #   current = nodes.pop(0)
    #   currentleft = current.left is not None
    #   currentright = current.right is not None

    #   cb(current.value)
    #   if currentleft:
    #     nodes.append(current.left)
    #   if currentright:
    #     nodes.append(current.right)

    q = []
    q.append(self)
    while len(q):
      current_node = q.pop(0) # pop from beginning; FIFO ordering; the first one added gets popped first
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      cb(current_node.value)
    

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
