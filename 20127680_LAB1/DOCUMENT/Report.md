

# Knight's tour problem 
# ======================
## 1. What is Knight’s Tour?
- On a chessboard, a knight's tour is a series of movements in which
the knight visits each square precisely once. The tour is closed if the
knight ends on a square one knight's move from the beginning
square (such that it can instantly tour the board again, following the
same path); otherwise, it is open

# Implementation
## 1. Backtracking
- Backtracking is an algorithmic strategy for recursively
solving problems by attempting to develop a solution progressively, one piece
at a time, and discarding any solutions that do not satisfy the problem's criteria
at any point in time (by time, here, is referred to the time elapsed till reaching
any level of the search tree).

### 1.1. Staistics
![Result table](/OUTPUT/result_backtrack.png)

- Comment:  
    - Because time complexity of backtracking is O(8𝑛2) – very huge giant number in real time. Therefor, in size 15x15 and 25x25 we compute the statistics based on 1-hour-long runs
### 1.3. Complexity
- Time complexity: O(8*n^2)
- Space complexity: O(n^2)

### 1.4. How to run
- Run the following command in the terminal:
```20127680.py -px 1 -py 1 -s 8```
-px: x-coordinate of the starting point
-py: y-coordinate of the starting point
-s: size of the board

## 2. Warnsdorff's rule
- Warnsdorff’s Heuristic: According to the Warndorff's Rule, we can start
from any initial location of the knight on the board and move to a neighboring,
unvisited square with a minimum degree (minimum number of unvisited
adjacent squares). This approach can be used to any graph in a broader sense

### 2.1. Staistics
![Result table](/OUTPUT/result_heuristic.png)

- Comment:  
    - Warnsdorff’s heuristic successfully finds a solution in linear time
    (O(n)).
    - The majority of cases will find solutions exceptions the existence of
    solutions in teacher’s file.

### 2.3. Complexity
- Time complexity: O(n)
- Space complexity: O(n^2)