import copy

# Landmark Heuristics Function
def heuristic(state):
    distance = 0
    for i in range(len(state) - 1):
        # current position pancake is not adjacent size to pancake below
        if abs(state[i] - state[i + 1]) > 1:
            distance += 1
    if state[len(state) - 1] != len(state):
        # size of bottom one differs from the size it supposed to be
        distance += 1
    return distance

# flip pancakes above i
def flip(state, i):
    newState = copy.copy(state)
    for step in range(round(i/2 + 0.1)):
        temp = newState[step]
        newState[step] = newState[i-step]
        newState[i-step] = temp
    return newState

# A star method
class AStarMethod:
    init = []
    size = None
    queue = []
    visited = []
    goal = None
    #[[Flips to reach the state], node state, backward cost, heuristic cost, total cost]
    def __init__(self, state):
        self.init = state
        self.size = len(state)
        self.queue = [[[], state, 0, heuristic(state), heuristic(state)]]
        self.visited = [state]

    # sort nodes based on backward cost and heuristic cost
    # i.e. based on total cost calculated by backward cost and heuristic cost
    def priority(self):
        for i in range(len(self.queue)):
            for j in range(i, len(self.queue)):
                if self.queue[i][4] < self.queue[j][4]:
                    temp = self.queue[i]
                    self.queue[i] = self.queue[j]
                    self.queue[j] = temp
        return True

    # expand node then add its children to the priority queue.
    def expand(self):
        # get expand node
        expandState = self.queue.pop()
        for i in range(1, self.size):
            newStep = copy.copy(expandState[0])
            newStep.append(i)
            newState = copy.copy(expandState[1])
            newState = flip(newState, i)
            newBackwardCost = expandState[2] + 1
            newForwardCost = heuristic(newState)
            newTotalCost = newForwardCost + newBackwardCost
            if newState not in self.visited:
                self.queue.insert(0, [newStep, newState, newBackwardCost, newForwardCost, newTotalCost])
                self.visited.append(newState)
        self.priority()
        return True

    # does solution exist
    def goaltest(self):
        if len(self.queue) == 0:
            self.goal = False
            return True

        for i in self.queue:
            if i[1] == list(range(1, self.size + 1)):
                self.goal = i
                return True

        return False

    # whole solution
    def run(self):
        while not self.goaltest():
            self.expand()
        return self.goal

    # show solutions
    def solution(self):
        if self.goal is not None:
            if self.goal == False:
                print("solution not exist")
                return True
            if len(self.goal[0]) == 0:
                print("initial state is good, we don't have to flip any pancake")
            else:
                print("need {} steps to sort given pancakes" .format(len(self.goal[0])))
                print("the initial pancakes state is: {}".format(str(self.init)))
            print("-------------------------------------------------------------------------")
            step = copy.copy(self.init)
            count = 0
            for i in self.goal[0]:
                count += 1
                i = copy.copy(i)
                step = flip(step, i)
                if i == 0:
                    print("step {}: flip pancakes at and above {}st position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                elif i == 1:
                    print("step {}: flip pancakes at and above {}nd position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                elif i == 2:
                    print("step {}: flip pancakes at and above {}rd position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                else:
                    print("step {}: flip pancakes at and above {}th position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
            return True
        return False

# uniform cost search
class UCSMethod:
    # The structure of one node in priority queue is [[Flips to reach the state], state of node, backward cost]
    init = []
    size = None
    visited = []
    queue = []
    goal = None

    def __init__(self, state):
        self.init = state
        self.size = len(state)
        self.queue = [[[], state, 0]]
        self.visited = [state]

    # Sort the priority queue based on backward cost
    def sort(self):
        for i in range(len(self.queue)):
            for j in range(i, len(self.queue)):
                if self.queue[i][2] < self.queue[j][2]:
                    temp = self.queue[i]
                    self.queue[i] = self.queue[j]
                    self.queue[j] = temp
        return True

    # expand node
    def expand(self):
        expandState = self.queue.pop()
        for i in range(1, self.size):
            newStep = copy.copy(expandState[0])
            newStep.append(i)

            newState = copy.copy(expandState[1])
            newState = flip(newState, i)

            newBackwardCost = expandState[2] + 1

            if newState not in self.visited:
                self.queue.insert(0, [newStep, newState, newBackwardCost])
                self.visited.append(newState)

        self.sort()
        return True

    # solution exists?
    def goaltest(self):
        if len(self.queue) == 0:
            self.goal = False
            return True
        for step in self.queue:
            if step[1] == list(range(1, self.size + 1)):
                self.goal = step
                return True
        return False

    # try to get solution
    def run(self):
        while not self.goaltest():
            self.expand()
        return self.goal

    # whole solution
    def solution(self):
        if self.goal is not None:
            if self.goal == False:
                print("solution not exist")
                return True
            if len(self.goal[0]) == 0:
                print("initial state is good, we don't have to flip any pancake")
            else:
                print("need {} steps to sort given pancakes" .format(len(self.goal[0])))
                print("the initial pancakes state is: {}".format(str(self.init)))
            print("-------------------------------------------------------------------------")
            step = copy.copy(self.init)
            count = 0
            for i in self.goal[0]:
                count += 1
                i = copy.copy(i)
                step = flip(step, i)
                if i == 0:
                    print("step {}: flip pancakes at and above {}st position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                elif i == 1:
                    print("step {}: flip pancakes at and above {}nd position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                elif i == 2:
                    print("step {}: flip pancakes at and above {}rd position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
                else:
                    print("step {}: flip pancakes at and above {}th position".format(count, i + 1))
                    print("new state: {}".format(str(step)))
            return True
        return False

if __name__ == "__main__":
    method = input("AStar or UCS (case-sensitive): ")
    strState = input("Input initial state (use comma to seperate numbers, for example: 1,2,3): ")
    state = list(map(int, strState.split(',')))
    if method == "AStar":
        p = AStarMethod(state)
        print("-------------------------------------------------------")
        print("use AStar to solve problem state {}".format(str(state)))
    elif method == "UCS":
        p = UCSMethod(state)
        print("-------------------------------------------------------")
        print("use UCS to solve problem state {}".format(str(state)))
    p.run()
    p.solution()
    print("finish")
