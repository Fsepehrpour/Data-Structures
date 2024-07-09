# Implement an Array data structure as a simplified type of list.
class Array():
  def __init__(self, size=10):  # constructor
    self._size = size  
    self._items = [None] * size    # the array stored as a list
    
    
  def __getitem__(self, index):             # return the value at index
    return self._items[index]
    

  def __setitem__(self, index, value):      # set the value at index
    self._items[index] = value
    
  def __len__(self):
    return self._size

  def clear(self, value=None):
    for i in range(len(slef._items)):
      self._items[i] = value

  def __iter__(self):
    for item in self._items:
      yield item


  
 
