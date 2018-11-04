'''
What is a heap?
- A data structure that enables us to represent a binary tree without using any pointers
- The parent node "dominates" its child nodes.
- Can be dominated by being smaller or larger. Depends on the type of heap tree. (min-heap or max-heap tree)

What is a Priority Queue?
- A data structure that allows elements to enter a system at arbitrary intervals
- TODO: Need to elaborate.

What are the basic operations of a Priority Queue?
- Insert
- Find_Minimum / Find_Maximum
- Delete_minimum / Delete_Maximum

If a priority queue is built using a heap, what are the runtime of it's operations?

'''

import math
import random

class PriorityQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.sizeOfQueue = 0

    def print(self):
        powerOfTwo = math.pow(1, 2)
        items = []
        for i in range(len(self.queue)):
            items.append(self.queue[i])
            if (len(items) == powerOfTwo):
                powerOfTwo *= 2
                print(items)
                items = []

        if (len(items) != 0):
            print(items)
        
# Constructing the heap
def pq_insert(pq, item):
    # Check if there's room in the Queue
    if (pq.sizeOfQueue >= len(pq.queue)):
        raise Exception("Error: priority queue is at capacity")

    # Insert at the left most avaiable index of the list. (Insert-A)
    index = pq.sizeOfQueue
    pq.queue[index] = item
    pq.sizeOfQueue += 1 

    # If needed, re-establish dominace ordering. (Insert-B)
    bubble_up(pq, index)

    return

def bubble_up(pq, index):
    # Checking if it the index is at the root
    parentIndex = get_parent_index(index)
    if parentIndex == -1:
        return

    # Check if the child dominates the parent
    if pq.queue[index] < pq.queue[parentIndex]:
        swap(pq, parentIndex, index)
        bubble_up(pq, parentIndex)

    return

def swap(pq, indexOne, indexTwo):
    temp = pq.queue[indexOne]
    pq.queue[indexOne] = pq.queue[indexTwo]
    pq.queue[indexTwo] = temp
    return

def get_parent_index(index):
    # For explanation, look at (Parent-A)
    return math.floor((index+1)/2) - 1 

# Snag this from the internet
def is_heap(A):
    return all(A[i] >= A[(i - 1) // 2] for i in range(1, len(A)))


# Removing the minimum element

# Heapsort

pq = PriorityQueue(31)
for x in range(len(pq.queue)):
    pq_insert(pq, random.randint(0, 100))

pq.print()

'''
Footnotes

(Insert-A)
- In order to be space efficient, we as few holes in our tree as possible.
- If so, only the last level may be incomplete and we want to pack the elements
  to the far left as possible.
- By doing this, we can represent a n-tree with exactly n elements of the array
- If we don't reenforce this, worst case, we need an array of size 2^n 
- Since the last level of the tree is always filled, the height of the tree is ln(n)

(Insert-B)
- When inserting a new element into the tree, the element can upset the domainance ordering of the heap
- We need to move the elements around in the tree to re-establish the dominance order
- The solution is to check if the newly added child is dominated by it's parent
  - If not, swap the child with the parent
  - Continue this check and swap until the element is dominated by it's parent or until its at the root node position


(Parent-A)
- rt = root, rtc1 = root child one, rtc2 = root child two

- [ 0,    1,    2,      3,        4,       5,       6,       7]
- [rt, rtc1, rtc2, rtc1 c1, rtc1 c2, rtc2 c1, rtc2 c2]

To find the parent of rtc1c2, we takes it's array index and divide it by 2 and math.floor it
rtc1c2 index is 5

5 / 2 = 2.5 = 2
''' 