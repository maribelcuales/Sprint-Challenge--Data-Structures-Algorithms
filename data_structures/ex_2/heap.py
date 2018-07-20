# def heapify(arr, n, i):
#   largest = i  #root 
#   left = 2 * i + 1
#   right = 2 * i + 2

#   if left < n and arr[i] < arr[left]:
#     largest = left
  
#   if right < n and arr[largest] < arr[right]:
#     largest = right

#   if largest != i:
#     arr[i], arr[largest] = arr[largest], arr[i] #swap

#     heapify(arr, n, largest)

def heapsort(arr):
  # initialize our heap
  heap = Heap()
  sorted = []

  for el in arr:
    heap.insert(el)
  
  while heap.get_size() > 0:
    sorted.append(heap.delete())  
  
  sorted.reverse()

  return sorted


  # heap = Heap()
  # # initialize our sorted array to have length equal to our input array
  # sorted = [0] * len(arr)

  # for el in arr:
  #   heap.insert(el)

  # for i in range (len(arr)):
  #   sorted[len(arr) - i - 1] = heap.delete()

  # return sorted


  # n = len(arr)

  # for i in range(n, -1, -1):
  #   heapify(arr, n, i)

  # for i in range(n - 1, 0, -1):
  #   arr[i], arr[0] = arr[0], arr[i] #swap
  #   heapify(arr, i, 0)


class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1