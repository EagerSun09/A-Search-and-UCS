Course:	     CS-131-Artificial Intelligence
Assignment:  AStar Search and Uniform Cost Search in Pancakes Problem
Name: 	     Yige Sun

I assume:
	i. The position of pancakes is 1 indexed.(The first position is 1.)

*******************************IMPORTANT NOTE*************************************
UCS method is a little bit slow to solve 10 pancakes. If it takes too long for you to test it, just try 5 pancakes. When
 number of pancakes is 5, UCS could give solution more quickly.
********************************STILL IMPORTANT*************************************
Since this will get information from the key board, the input is case-sensitive(i.e. AStar is different from astar).
When choosing AStar Approach or USC Approach, you should strictly type AStar or USC. When typing initial state,
use comma to seperate numbers.
Example:
use AStar or UCS (case-sensitive): AStar
Input initial state (use comma to seperate numbers, for example: 1,2,3): 2,3,4,5,1
*****************************************************************************************

AStar Approach:
	i.   Heuristic Function h(n): The number of stack positions for which the pancake at that position is not of 
			 adjacent size to the pancake below.
	ii.  Backward Cost Function g(n): How many times we need to flip pancakes to get the node from initial state.
	iii.  Total Cost Function f(n)=h(n)+g(n)
	iv. Nodes Expansion: Expand the node with the lowest f(n)
	v.  Procedure:
		a) Add initial state into priority queue.
		b) While solution has not been found, we repeatedly do actions c~e.
		c) If priority queue is empty, this means we have nothing to expand, return failed.
		d) If priority queue is not empty, we pop the node with smallest f(n) out from priotity queue and
		    add its child nodes into priority queue.
		e)  Sort priority queue based on f(n).(i.e. Node with smaller result of g(n) will be poped out earlier.)
		f)  Get and show solution.

Uniform Cost Search:
	i.  Backward Cost Function g(n):  How many times we need to flip pancakes to get the node from initial state.
	ii.  Node Expansion: Expand the node with the lowest g(n).
	iii. Procedure:
		a) Add initial state into priority queue.
		b) While solution has not been found, we repeatedly do actions c~e.
		c)  If priority queue is empty, this means we have nothing to expand, return failed.
		d) If prority queue is not empty, we pop the node with smallest g(n) out from priority queue and
		     add its child nodes into the priority queue.
		e) Sort the priority queue based on g(n).(i.e. Node with smaller result of g(n) will be poped out earlier.)
		f)  Get and show solution.
