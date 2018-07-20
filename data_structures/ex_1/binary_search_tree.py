class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    hasleft = self.left is not None
    hasright = self.right is not None

    cb(self.value)    
    if hasleft:
      self.left.depth_first_for_each(cb)
    if hasright:
      self.right.depth_first_for_each(cb)
    return


  def breadth_first_for_each(self, cb):    
    nodes = [self]

    while len(nodes) > 0:
      current = nodes.pop(0)
      currentleft = current.left is not None
      currentright = current.right is not None

      cb(current.value)
      if currentleft:
        nodes.append(current.left)
      if currentright:
        nodes.append(current.right)
    

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
