## First Exam Poll Everywhere Review

**What is the process of looking for a sequence of actions that reaches the goal?**  
Search

**Which of these does NOT influence the state space?**  
Goal

**What does it mean if a heuristic is admissible?**  
It never over-estimates the true cost to the goal.

**What is the output of a heuristic funtion for some node n?**  
An estimate of the cost from n to the goal.

**What node will DFS expand?**  
Node with the largest depth.

**What node will UCS expand?**  
Lowest path cost.

**What condition makes A\* and UCS expand nodes exactly the same?**  
  h(n) = constant

**Note:** The professor likes this question and hinted at there possibly being a question(s) similar to it on the exam. Make sure to study conditions that make algorithms behave similarly.

**What node will A\* expand?**  
  Lowest f cost.

**What factors influence the time complexity of A\*?**  
  Depth of the goal.
  Heuristic error.
  Branching factor.

**Note:** "Path cost error" was the only incorrect option. Know the time complexity of A*.

**How is the time complexity of A\* classified?**  
  Exponential

**What is the solution for a classical search algorithm (A\*, BFS, ect.)?**
  Path

**What is a solution for local search algorithms?**  
  State

**Note:** "Goal" is not a solution because:
 1) there can be many goals
 2) you may never reach any goal

**What node will greedy search expand?**  
  Lowest heuristic cost.

**Note:** Greedy search only cares about heuristic cost, nothing else.

**What is the main problem when using Hill Climbing based algorithms?**
  Local minima/maxima.

**In simulated annealing, how is the "next" node chosen?**
  Uniformly sampled.

**Note:** Uniformly sampled because you're randomly selecting a node from a list of successors. You're not using heuristic cost when selecting a node, only when comparing against current node.

**In genetic algorithms, how are the "parents" chosen when doing a crossover operation?**
  Randomly selected based on fitness values.

**In genetic algorithms, how are states represented?**
  String of numeric values.

