from gurobipy import *
import sys


problem = sys.argv[1]

m = Model()
m.Params.LogFile = problem + '.log'

with open(problem + '.txt') as reader:
    for line in reader:
        spl = line.split()
        if spl[0] == "p":
            nodes = m.addVars(int(spl[2]), vtype=GRB.BINARY)
        else:
            e1 = int(spl[1])-1
            e2 = int(spl[2])-1
            m.addConstr(nodes[e1]+nodes[e2] <= 1)



try:
    with open(problem + '.initial') as reader:
        for line in reader:
            for v in line.split():
                nodes[int(v)-1].Start = 1
    m.Params.Heuristics = 0
except:
    pass

m.setObjective(nodes.sum(), GRB.MAXIMIZE)

# m.Params.Presolve = 2
# m.Params.MIPFocus = 3
m.Params.NodefileStart = 0.5
m.Params.Threads = 8
# m.Params.Cuts = 2
m.Params.ResultFile = problem + '.sol'

# m.tune()
m.optimize()
