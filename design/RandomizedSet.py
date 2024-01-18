"""
date: 2024.01.17
author: @adambechtold
interviewer: @badr-elmazaz
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/Wtb1HnEZNT

# Lessons
	- Python Classes
    - Syntax - Define and initialize variables in a class
    - Syntax - Reference values within a class
  - Practical application of Average, Best, and Worst Case
  - New Methods
    - random.choice
    - list.pop
    - hashmap.pop

# Problem
Implement the RandomizedSet class:

RandomizedSet() 
Initializes the RandomizedSet object.

bool insert(int val) 
	Inserts an item val into the set if not present. 
  Returns true if the item was not present, false otherwise.
  
  # Examples
  ## Empty Set
  - start: {}
  - input: 1
  - output: true
  
  ## Not in set
  - start: {2}
  - input: 1
  - output: true
    
  ## Already in set
  - start: {1,2,4}
  - input: 2
  - output: false
  
bool remove(int val) 
	Removes an item val from the set if present. 
  Returns true if the item was present, false otherwise.
  
  ## Empty Set
  - start: {}
  - input: 1
  - output: false
  - end: {}
  
  ## Not in set
  - start: {2}
  - input: 1
  - output: false
  - end: {}
    
  ## Already in set
  - start: {1,2,4}
  - input: 2
  - output: true
  - end: {1,4}

int getRandom() 
	Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
  Each element must have the same probability of being returned.
  
  # Examples
  ## Already in set
  - start: {1,2,4}
  - input: N/A
  - output: 1, 2, or 4. Equal chance of each
  - end: {1,4}

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random

class RandomizedSet:
    
  def __init__(self):
    self.values = []

    self.indexes_by_value = {} 
    #  Key: Value
    #  Value: Index of that value in the list of values

  def insert(self, val: int) -> bool:
    has_val = val in self.indexes_by_value
    
    if has_val:
      return False  # we did not insert the value
    else:
      self.values.append(val)
      self.indexes_by_value[val] = len(self.values) - 1
      return True # we inserted the value
    
    
  def remove(self, val: int) -> bool:
    has_val = val in self.indexes_by_value
    
    if not has_val:
      return False
    
    # let's remove it
    ## get the index of the value
    index_of_val = self.indexes_by_value[val] 

    ## put the value at the end of the array
    last_index = len(self.values) - 1  
    value_at_end = self.values[last_index]

    ## swap the values
    self.values[index_of_val] = value_at_end 
    self.indexes_by_value[value_at_end] = index_of_val 

    ## remove last value in the list
    self.values.pop() # [1,3]
    self.indexes_by_value.pop(val)

    return True


  def getRandom(self) -> int:
    return random.choice(self.values)




"""
# Test Case
add 1        [1] {1:0}
add 2        [2] 
add 3				[1,2,3] {1:0, 2:1, 3:2}
remove 2    has_val = true...   ind
add 2       
"""




























