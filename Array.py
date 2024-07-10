# Implement an Array data structure as a simplified type of list.
class Array():
  def __init__(self, capacity=10):  # constructor
    self._capacity = capacity
    self._items = [None] * capacity    # the array stored as a list
    self._size = 0 


  def __getitem__(self, index):             # return the value at index
    return self._items[index]


  def __setitem__(self, index, value):      # set the value at index
    if index < 0 or index >= self._size:
      raise IndexError("Index is out or range")
    self._items[index] = value

  def __len__(self):
    return self._size

  def clear(self, value=None):
    for i in range(len(slef._items)):
      self._items[i] = value

  def __iter__(self):
    for item in self._items:
      yield item

  def insert(self, value):
    if self._size == self._capacity:
      self._resize()
    self._items[self._size] = value
    self._size += 1

  def _resize(self):
    print(f"Resizing from {self._capacity} to {self._capacity * 2}")
    new_capacity = self._capacity * 2
    new_items = [None] * new_capacity
    for i in range(self._size):
      new_items[i] = self._items[i]
    self._items = new_items
    self._capacity = new_capacity

  def find(self, item):
    for i in range(self._size):
      if self._items[i] == item:
        return i
    return -1
  
  def delete(self, index):
    if index < 0 or index >= self._size:
      raise IndentationError("Index is not in range")
    for i in range(index, self._size - 1):
      self._items[i] = self._items[i + 1]
      self._size -= 1

  def traverse(self):
    for i in range(self._size):
      print(self._items[i], end=' ')
    print()
  def __iter__(self):
    for i in range (self._size):
      yield self._items[i]
  
  def __repr__(self):
    return '[' + ', '.join(str(item) for item in self) + ']'



  
 
