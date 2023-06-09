# Queue-using-Single-Linked-List-and-3-Array-Alternative-Python
This Implements 4 Types of Queue with Command Line Interace using python

## TYPES OF QUEUE THAT IS AVAILABLE IN THE INTERFACE:

| Queue Types | Implementation | How it Works |
| --- | --- | --- |
| Type 0 | Queue that implements Single Linked List. | It uses Nodes and Single Linked List data structure to create the Queue. Basically, each time an element is added, the pointer called link inside a recent added element node is assigned to point to the newest element node, then the tail pointer is assigned to point into it. The head pointer always point to the oldest created element node and are assigned to a new node only when the node is empty prior to the element node addition. |
| Type 1 | Queue that implements Array. | It functions by adding elements into the array and when the elements is removed, the entire elements got shifted to the very first index of the array. The head pointers always point to index 0 of the array, while the tail pointer always move according to the number of elements is inside the array. |
| Type 2 | Queue that implements Array. | It functions by adding elements into the array and when the elements is removed, nothing happend to the array (only the oldest element got removed and the head pointer move to the next elements. Note, the head pointer got resetted to index 0 when the pointer is at the end of the array during an element removal process,). However, if the array is full and the index 0 of the array is also empty during the element addition process, the entire elements got shifted to the very first index of the array, the head pointer is made to point the first index of the array, and then the tail pointer is made to point to the last element added into the array. |
| Type 3 | Queue that implements Array. | It functions by adding elements into the array and when the elements is removed, the head pointer move to the next index of the array. The tail pointer also move to the next array index when new element is added into the array. Notes: During the addition process, if the tail pointer reached the end of the array and the index 0 of the array is empty, the tail pointer will point to the index 0 of the array and add the element there. During the removal process, if the head pointer reached the end of the array, it will be sent back to the index 0 of the array. |

## Available Command for the CLI
| Command | Parameters | Function |
| --- | --- | --- |
| showInstance | (No Parameter) | To show created Instance of an Queue. |
| isEmpty | (Queue Name) | To check if the selected Queue is Empty. |
| isFull | (Queue Name) | To check if the selected Queue is Full. |
| nbElmt | (Queue Name) | To check the number of element added in the selected Queue. |
| createEmpty | (Queue Type, Queue Name, Queue Size) | To create an Queue with the type available in the table above. |
| Add | (Queue Name, Element) or (Queue Name, [Element0, Element1, .... Elementn]) | to add a single or many element into the selected Queue. |
| Del | (Queue Name) or (Queue Name, Number to Take) | To take an element or elements from the selected Queue. |
| remove | (Queue Name) | To remove Queue Instance from the program Dictionary |

## Important Note! The program mainly use Indonesian Language for the CLI!
The program also has no inbuilt language selector. If anyone want to add that to this Repo, feel free to pull a request <3.

## Happy Happy Coding!
-Sincerely, Alif (KK93)
