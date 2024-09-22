"""
Dynamic Array

link: https://neetcode.io/problems/dynamicArray
whiteboard: none
author: adambechtold
date: 2024-09-22
"""


class DynamicArray:
    # elements: list - storage for elements of our array
    # i_end: int | None - the position of the last element in elements

    def __init__(self, capacity: int):
        # initialize array with size of capacity
        #  - Assumption: capacity > 0
        self.elements = [None] * capacity
        self.i_end = -1

    def get(self, i: int) -> int:
        # return the element at i
        # Assume i is valid.

        # Approach - have a list, get the i_th element - elements[i]
        #   - Runtime: O(1)
        #   - Memory: O(1)

        return self.elements[i]

        # Approach - Have a linked list, walk through each position to get to that element
        #   - Runtime: O(n)
        #   - Memory: O(1)
        # Variant - Have a linked list and an array; The array points to a node in the linked list
        #    Kind of the same as the first approach with just a list

    def set(self, i: int, n: int) -> None:
        # set the element at index i to value n
        # Assume i is valid (0 <= i <= i_end.length)

        """
        Approach - have a list, set the i_th element - element[i] = n
          - Runtime: O(1)
          - Memory: O(1)

        List Capacity = 4
            1,2,_,_
        Set(3, 4)
            invalid - the  0 <= i provided by set(i) < # elements in array
        """

        self.elements[i] = n

    def pushback(self, n: int) -> None:
        # push value n to the end of the array
        # assume array is non-empty

        """
        Approach - have a list, track the end of the list (i_end), set the i_end_th element
           element[i_end] = n; i_end++
           ⚖️ Consideration - Should i_end track the position of the last element or the next empty spot?
           - Runtime: O(1)
           - Memory: O(1)

        List Capacity = 4
            1,_,_,_
        Pushback (2)
            1,2,_,_
        """
        max_index = len(self.elements) - 1  # 1 - 1 = 0
        next_index = self.i_end + 1  # 1
        if next_index > max_index:
            self.resize()
        self.set(next_index, n)
        self.i_end = next_index

    def popback(self) -> int:
        # pop and return the element at the end of the array
        # Assume the array is not empty

        """
        Capacity = 4
            1,2,3_
        popback()
            returns 3
            elements = 1,2,_,_
            i_end = 1
        """

        last_element = self.elements[self.i_end]

        self.elements[self.i_end] = None
        self.i_end = self.i_end - 1  # could this ever go to -1?

        return last_element

        # Approach - have a list, track the end of the list (i_end), return element[i_end], i_end--
        #   - Runtime: O(1)
        #   - Memory: O(1)

    def resize(self) -> None:
        # double the capacity of the array
        # ? - even if array is pretty much empty?

        # Approach - Have a list, create a new list, copy all elements from the old list into the new list
        #    - Runtime: O(n)
        #    - Memeory: O(2n) = O(n)

        new_elements = [None] * (self.getCapacity() * 2)
        for i in range(len(self.elements)):
            new_elements[i] = self.elements[i]

        self.elements = new_elements

        # Approach - Have a linked list, capacity is just a "limit"; Simply increase the limit 2x
        #   - Runtime: O(1)
        #   - Memory: O(1)

    def getSize(self) -> int:
        # number of elements in the array
        return self.i_end + 1

    def getCapacity(self) -> int:
        # return the capacity of the array

        # Approach - List, just get the length of the array

        return len(self.elements)

        # Approach - Linked List, return the "capacity" variable


"""
Approach - Track as an array
- Most operations are O(1) runtime
- Resize is O(n)
The overall, amortized runtime is O()

1,2
1,2,_,_  Runtime was 4 operations for 2 elements O(2n)

1,2,3,4
1,2,3,4,_,_,_,_ 
Runtime: 
    - add 3 & 4 - 2
    - Copy all elements - 4
    - 6 operations over 4 elements 

1,2,3,4,5,6,7,8
1,2,3,4,5,6,7,8,_,_,_,_,_,_,_,_
Runtime:
    - add 5-8 - 4
    - copy all elements - 8
    - 12 operations over 8 elements

I think, if I remember correctly, this is O(N), but honestly I don't totally remember...


Approach - Track as a linked list
- Get()/Set() are O(n) 👎
- Resize is O(1)
Variant - Track as a linked list with a hashmap to track location of elements
- Get()/Set() are O(1)
- Resize is O(1)

"""
