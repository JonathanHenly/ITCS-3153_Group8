## First Exam Poll Everywhere Review

Q: What is the process of looking for a sequence of actions that reaches the goal?

A: Search.

Q: Which of these does NOT influence the state space?

A: Goal.

Q: What does it mean if a heuristic is admissible?

A: It never over-estimates the true cost to the goal.

Q: What is the output of a heuristic funtion for some node n?

A: An estimate of the cost from n to the goal.

Q: What node will DFS expand?

A: Node with the largest depth.

Q: What node will UCS expand?

A: Lowest path cost.

Q: What condition makes A* and UCS expand nodes exactly the same?

A: h(n) = constant.

Note: Professor likes this question and hinted at there possibly being a question(s) similar to it on the exam. Make sure to study conditions that make algorithms behave similarly.

Q: What node will A* expand?

A: Lowest f cost.

Q: What factors influence the time complexity of A*?

A: Depth of the goal.

A: Heuristic error.

A: Branching factor.

Note: "Path cost error" was the only incorrect option. Know the time complexity of A*.

Q: How is the time complexity of A* classified?

A: Exponential.

Q: What is the solution for a classical search algorithm (A*, BFS, ect.)?

A: Path.

Q: What is a solution for local search algorithms?

A: State.

Note: "Goal" is not a solution because:

      1) there can be many goals

      2) you may never reach any goal

Q: What node will greedy search expand?

A: Lowest heuristic cost.

Note: Greedy search only cares about heuristic cost, nothing else.

Q: What is teh main problem when using Hill Climbing based algorithms?

A: Local minima/maxima.

Q: In simulated annealing, how is the "next" node chosen?

A: Uniformly sampled.

Note: Randomly selecting a node from a list of successors, not using heuristic cost when selecting a node, only use heuristic when comparing against current node.

Q: In genetic algorithms, how are the "parents" chosen when doing a crossover operation?

A: Randomly selected based on fitness values.

Q: In genetic algorithms, how are states represented?

A: String of numeric values.

