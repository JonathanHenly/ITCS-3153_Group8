## First Exam Poll Everywhere Review

**What is the process of looking for a sequence of actions that reaches the goal?**  
- [x] Search

**Which of these does NOT influence the state space?**  
- [ ] Initial state
- [ ] Actions
- [ ] Transition model
- [x] Goal
- [ ] State representation

**What does it mean if a heuristic is admissible?**  
- [x] It never over-estimates the true cost to the goal.
- [ ] It always under-estimates the true cost to the goal.

> **Note:** "never over-estimates" and "always under-estimates" appear to be saying the same thing. However, "never over-estimates" implies it's possible for the estimation to equal true cost, while "always under-estimates" implies the estimation can never equal the true cost.

**What is the output of a heuristic funtion for some node n?**  
- [ ] The step cost from n to the goal.
- [ ] An estimate of the cost from n to the next node.
- [x] An estimate of the cost from n to the goal.
- [ ] An estimate of the cost from n to the start node.

**What node will DFS expand?**  
- [x] Node with the largest depth.
- [ ] Node with the least depth.
- [ ] Node with best heuristic cost.
- [ ] Randomly selected node.


**What node will UCS expand?**  
- [ ] Least depth.
- [ ] Lowest heuristic cost.
- [ ] Lowest step cost.
- [x] Lowest path cost.

**What condition makes A\* and UCS expand nodes exactly the same?**  
- [x] h(n) = constant
- [ ] h(n) = depth
- [ ] h(n) is admissible
- [ ] h(n) = linear function
> **Note:** The professor likes this question and hinted at there possibly being a question(s) similar to it on the exam. Make sure to study conditions that make algorithms behave similarly.

**What node will A\* expand?**  
- [ ] Lowest step cost.
- [ ] Lowest g cost.
- [x] Lowest f cost.
- [ ] Lowest h cost.


**What factors influence the time complexity of A\*?**  
- [x] Depth of the goal.
- [x] Heuristic error.
- [ ] Path cost error.
- [x] Branching factor.
> **Note:** "Path cost error" was the only incorrect option. Know the time complexity of A*.

**How is the time complexity of A\* classified?**  
- [ ] Factorial
- [ ] Linear
- [x] Exponential
- [ ] Quadratic

**What is the solution for a classical search algorithm (A\*, BFS, ect.)?**  
- [ ] Goal node
- [x] Path
- [ ] Actions
- [ ] Transition model

**What is a solution for local search algorithms?**  
- [ ] Initial
- [x] State
- [ ] Goal
- [ ] Heuristic
> **Note:** "Goal" is not a solution because:
> 1) there can be many goals
> 2) you may never reach any goal

**What node will greedy search expand?**  
- [x] Lowest heuristic cost.
- [ ] Lowest path cost.
- [ ] Largest f value.
- [ ] Lowest step cost.  
> **Note:** Greedy search only cares about heuristic cost, nothing else.

**What is the main problem when using Hill Climbing based algorithms?**  
- [ ] Constant heuristic costs.
- [ ] High time complexity.
- [ ] High space complexity.
- [x] Local minima/maxima.

**In simulated annealing, how is the "next" node chosen?**  
- [ ] Lowest heuristic cost.
- [x] Uniformly sampled.
- [ ] Local minima.
- [ ] Sample based on heuristic cost.
> **Note:** Uniformly sampled because you're randomly selecting a node from a list of successors. You're not using heuristic cost when selecting a node, only when comparing against current node.

**In genetic algorithms, how are the "parents" chosen when doing a crossover operation?**  
- [ ] Randomly selected with equal probability.
- [x] Randomly selected based on fitness values.
- [ ] Two highest fitness values.
- [ ] Two lowest fitness values.

**In genetic algorithms, how are states represented?**  
- [x] String of numeric values.
- [ ] String of bits.
- [ ] String of characters.
- [ ] 2D lists.
