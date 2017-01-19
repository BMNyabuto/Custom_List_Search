class BinarySearch(list):
  """A customised binary search method in an in-built Python List structure"""
  
  length = 0
  
  def __init__(self, a,b):
    list.__init__(self, range(b,((a*b) +b), b))
    self.length = ((a*b)/b)
    
  def search(self, Value_to_Find):
    countt = 0
    firstItem_index = 0
    lastItem_index = len(self)-1
    Present = False
    
    while firstItem_index<=lastItem_index and not Present:
      countt += 1
      midpoint = (firstItem_index + lastItem_index)//2
      
      if self[midpoint] == Value_to_Find:
        Present = True
      else:
        if Value_to_Find < self[midpoint]:
          lastItem_index = midpoint-1
          
        else:
          firstItem_index = midpoint+1
              
    if Present == True:
      return dict(count = countt, index = self.index(Value_to_Find))
    else:
      return dict(count = countt, index = -1)


