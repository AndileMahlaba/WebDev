class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned

class _BinTreeNode:
    def __init__(self, element):
        self._element = element  # node value
        self._right = None  # pointer to the right child
        self._left = None  # pointer to the left child

class BinaryTree:
    def __init__(self, root):  # BinaryTree initializes the root to a node with a value
        self._root = _BinTreeNode(root)

    def preOrder(self, start):
        # start at root->left-> right
        if start:
            print(start._element)
            self.preOrder(start._left)
            self.preOrder(start._right)

    def inOrder(self, start):
        # start left -> root -> right
        if start:
            self.inOrder(start._left)
            print(start._element)
            self.inOrder(start._right)

    def postOrder(self, start):
        # start left-> right -> root
        if start:
            self.postOrder(start._left)
            self.postOrder(start._right)
            print(start._element)

    def breadthFirst(self):
        # level by level
        q = ArrayQueue()
        q.enqueue(self._root)
        while not q.is_empty():
            node = q.dequeue()
            print(node._element)
            if node._left is not None:
                q.enqueue(node._left)
            if node._right is not None:
                q.enqueue(node._right)

#           1
#          / \
#         2   3
#        / \   \
#       4   5   6

myTree = BinaryTree(1)
myTree._root._left = _BinTreeNode(2)
myTree._root._right = _BinTreeNode(3)
myTree._root._left._left = _BinTreeNode(4)
myTree._root._left._right = _BinTreeNode(5)
myTree._root._right._right = _BinTreeNode(6)
print("***************************************************PREORDER TRAVERSAL")
myTree.preOrder(myTree._root)  # 1 2 4 5 3 6
print("****************************************************INORDER TRAVERSAL")
myTree.inOrder(myTree._root)
print("****************************************************POSTORDER TRAVERSAL")
myTree.postOrder(myTree._root)
print("****************************************************BREADTH FIRST TRAVERSAL")
myTree.breadthFirst()
