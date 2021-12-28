from pulp import *
import sys

def main(argv):

    if len(argv) != 3:
        print("Usage: python3 " + argv[0] + " <input filename> <total num of tables>")
        sys.exit(1)
    input_file = argv[1]
    num = int(argv[2])
    table_per_stage = 2

    f = open(input_file, 'r')
    prob = LpProblem("Scheduling Problem", LpMinimize)
    cost = LpVariable("Obj cost", lowBound=0, cat=LpInteger)
    for i in range(num):
        program = 'T' + str(i) + '= LpVariable(' + '\"' + 'T' + str(i) + '\"' + ', lowBound=0, cat=LpInteger)'
        # print(program)
        exec(program)
    # Objective function
    prob += cost, 'Objective function'
    # Constraints
    for i in range(num):
        prob += cost >= locals()['T' + str(i)]
    f = open(input_file, 'r')
    for line in f:
        if line == "\n":
             continue
        line = line.split('\n')[0]
        src = line.split(' ')[0]
        dst = line.split(' ')[1]
        prob += locals()[dst] - locals()[src] >= 1
    #for i in range(num):
    #    prob += lpSum(locals()['T' + str(j)] for j in range(num)) <= table_per_stage
            # prob += abs(locals()['T' + str(i) for i in range()] - locals()['T' + str(j)]) >= 1
    # print("prob =", prob)
    prob.solve()
    #for i in range(num):
    #    print("T"+str(i)+" value:", locals()['T'+str(i)].varValue)
    print("cost value:", cost.varValue)

if __name__ == '__main__':
    main(sys.argv)
