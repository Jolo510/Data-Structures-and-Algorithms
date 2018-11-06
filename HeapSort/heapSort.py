'''
Quiz and Recall Questions

1. Explain selection sort.

2. Explain the runtime of selection sort.

3. What is a Priority Queue?
Priority queue is like a normal queue but each element has a priority
associated with it.

4. What data stuctures can you use to efficiently implement a priority queue?
- Heap
- Balanced Binary Tree

5. What are the basic operations of a Priority Queue and their runtimes?
(If implemented by a heap or balanced search tree)
- Insert
- Find_Minimum / Find_Maximum
- Delete_minimum / Delete_Maximum

6. What is a heap?
- A data structure that enables us to represent a binary tree without using any pointers
- The parent node "dominates" its child nodes.
- Can be dominated by being smaller or larger. Depends on the type of heap tree. (min-heap or max-heap tree)

7. In the scenario of Heapsort, why is using a heap to implemented a 
priority queue better than using a balance binary tree?

8. Describe how you would insert a new element into a heap and maintain it's structure.

9. Describe how you would extract the minimum element from a heap and maintain it's structure.


It is an in-place sort, meaning it uses no extra memory over the array containing the elements to be sorted
'''

import math
import random

class PriorityQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.numberOfQueueElements = 0

    def print(self):
        powerOfTwo = math.pow(1, 2)
        items = []
        for i in range(self.numberOfQueueElements):
            items.append(self.queue[i])
            if (len(items) == powerOfTwo):
                powerOfTwo *= 2
                print(items)
                items = []

        if (len(items) != 0):
            print(items)
        
'''
Constructing the Heap
''' 
def pq_insert(pq, item):
    # Check if there's room in the Queue
    if (pq.numberOfQueueElements >= len(pq.queue)):
        raise Exception("Error: priority queue is at capacity")

    # Insert at the left most avaiable index of the list. (Insert-A)
    index = pq.numberOfQueueElements
    pq.queue[index] = item
    pq.numberOfQueueElements += 1 

    # If needed, re-establish dominace ordering. (Insert-B)
    bubble_up(pq, index)

    return

def bubble_up(pq, index):
    # Checking if it the index is at the root
    parentIndex = pq_parent_index(index)
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

def pq_parent_index(index):
    # For explanation, look at (Parent-A)
    return math.floor((index+1)/2) - 1 

'''
Extracting the Minimum
'''
def extract_minimum(pq):
    if (pq.numberOfQueueElements <= 0):
        raise("empty queue")
    else:
        minElement = pq.queue[0]
        pq.queue[0] = pq.queue[pq.numberOfQueueElements - 1]
        pq.numberOfQueueElements = pq.numberOfQueueElements - 1 
        bubble_down(pq, 0)

    return minElement

def pq_child_index(index):
    # For Explanation, look at (Child-A)
    return ((index + 1) * 2)-1

def bubble_down(pq, index):
    child_index = pq_child_index(index)
    min_index = index
    
    # Find the element that is lease dominate
    for i in range(2):
        if (child_index + i < pq.numberOfQueueElements):
            if (pq.queue[min_index] > pq.queue[child_index + i]):
                min_index = child_index + i

    # Or the children index of the index passed in is out of range
    if (min_index != index):
        swap(pq, index, min_index)
        bubble_down(pq, min_index)

# Heapsort

pq = PriorityQueue(25)
for x in range(len(pq.queue)):
    pq_insert(pq, random.randint(-50,50))

def heap_sort(listOfElements):
    
    pq = PriorityQueue(len(listOfElements))

    for current in listOfElements:
        pq_insert(pq, current)
    
    for i in range(len(listOfElements)):
        listOfElements[i] = extract_minimum(pq)

listOfRandomInts = []
for x in range(25):
    listOfRandomInts.append(random.randint(0,100))

heap_sort(listOfRandomInts)
print(listOfRandomInts)


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

- [ 0,    1,    2,      3,        4,       5,       6]
- [rt, rtc1, rtc2, rtc1 c1, rtc1 c2, rtc2 c1, rtc2 c2]

To find the parent of rtc1c2, we takes it's array index and divide it by 2 and math.floor it
rtc1c2 index is 5

5 / 2 = 2.5 = 2

(Child-A)
- [ 0,    1,    2,      3,        4,       5,       6,       7]
- [rt, rtc1, rtc2, rtc1 c1, rtc1 c2, rtc2 c1, rtc2 c2]

To find the child of a parent index, we take the parents index and multiply it by 2.
That'll give use the 1st child of the parent. 

To get the second child, we add one to the index of the first child.

Note: To account for the 0-index, I add one to the parent index, then subtract one from the result
''' 