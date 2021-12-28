import sys

def main(argv):
    if len(argv) != 3:
        print("Usage: python3 " + argv[0] + " <input filename> <total num of tables>")
        sys.exit(1)
    input_file = argv[1]
    num = int(argv[2])

    table_list = []
    # generate list of table
    for i in range(num):
        table_list.append("T" + str(i))
    # parse the input file
    dep_graph = {} # key: table name, val: a series of tables that are dependent on key table
    in_degree = {} # key: table name, val: how many tables the key is dependent on directly
    for table in table_list:
        in_degree[table] = 0
        dep_graph[table] = []

    f = open(input_file, 'r')
    for line in f:
        if line == "\n":
            continue
        line = line.split('\n')[0]
        src = line.split(' ')[0]
        dst = line.split(' ')[1]
        in_degree[dst] += 1
        if src in dep_graph:
            dep_graph[src].append(dst)
    # print(dep_graph)

    table_limit = 2
    stage_num = 0
    # allocation (assume there is no limit of tables available per stage)
    while(len(dep_graph) != 0):
        curr_list = []
        for t in dep_graph:
            if in_degree[t] == 0 and len(dep_graph[t]) > 0:
                curr_list.append(t)
                if len(curr_list) == table_limit:
                    break
        # Fill in other positions
        if len(curr_list) < table_limit:
            for t in dep_graph:
                if in_degree[t] == 0 and t not in curr_list:
                    curr_list.append(t)
                if len(curr_list) == table_limit:
                    break
        for mem_table in curr_list:
            for following_tb in dep_graph[mem_table]:
                in_degree[following_tb] -= 1
            del dep_graph[mem_table]
        print(curr_list)
        stage_num += 1
    print("maximum stage number (0 based) is :", stage_num - 1)

if __name__ == '__main__':
    main(sys.argv)
