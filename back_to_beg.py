import sys
import copy

table_limit_per_stage = 2
def compare(t1):
    return out_degree_cp[t1]

def main(argv):
    if len(argv) != 3:
        print("Usage: python3 " + argv[0] + " <input file> <num of tables>")
        sys.exit(1)
    input_file = argv[1]
    num = int(argv[2])

    table_list = []
    # generate list of table
    for i in range(num):
        table_list.append("T" + str(i)) 
    # parse the input file
    dep_graph = {} # key: table name, val: a series of tables that the key is dependent on  -->key
    inf_graph = {} # key: table name, val: a series of tables that are dependent on key table
    out_degree = {} # key: table name, val: how many tables that are dependent on key directly
    in_degree = {} # key: table name, val: how many tables the key is dependent on directly
    for table in table_list:
        out_degree[table] = 0
        dep_graph[table] = []
        in_degree[table] = 0
        inf_graph[table] = []

    f = open(input_file, 'r')
    for line in f:
        if line == "\n":
            continue
        line = line.split('\n')[0]
        src = line.split(' ')[0]
        dst = line.split(' ')[1]
        out_degree[src] += 1
        in_degree[dst] += 1
        dep_graph[dst].append(src)
        inf_graph[src].append(dst)
    global out_degree_cp 
    out_degree_cp = copy.deepcopy(out_degree)
    table_len_dic = {} # key: len, val: a series of tables at that position
    curr_len = 0
    while (len(table_list)):
        table_len_dic[curr_len] = []
        for table in table_list:
            if out_degree[table] == 0:
                table_len_dic[curr_len].append(table)
        for table in table_len_dic[curr_len]:
            table_list.remove(table)
            for mem in dep_graph[table]:
                out_degree[mem] -= 1
        curr_len += 1
    for i in range(curr_len):
        table_len_dic[i].sort(reverse=True,key=compare)
    print(table_len_dic)
    curr_len -= 1
    stage_num = 0
    pos = 0
    # allocation to stages
    while (curr_len >= 0):
        curr_list = []
        # TODO:Fill in the curr_list
        curr_len_tmp = curr_len
        while (len(curr_list) < table_limit_per_stage):
            if pos >= len(table_len_dic[curr_len_tmp]):
                pos = 0
                curr_len_tmp -= 1
                if curr_len_tmp < 0:
                    break
            else:
                if curr_len_tmp == curr_len:
                    to_append_table = table_len_dic[curr_len_tmp][pos]
                    curr_list.append(to_append_table)
                    table_len_dic[curr_len_tmp].remove(to_append_table)
                else:
                    if in_degree[table_len_dic[curr_len_tmp][pos]] == 0:
                        to_append_table = table_len_dic[curr_len_tmp][pos]
                        curr_list.append(to_append_table)
                        table_len_dic[curr_len_tmp].remove(to_append_table)
                    else:
                        pos += 1
        print(curr_list)
        # TODO: update the in_degree
        for table in curr_list:
            for mem in inf_graph[table]:
                in_degree[mem] -= 1
        # TODO: find next len
        while (curr_len >= 0):
            if len(table_len_dic[curr_len]) > 0:
                break
            curr_len -= 1
        pos = 0
        stage_num += 1
    # curr_len = the largest key of table_list + 1
    print("Max value of stage (0 based) is:", stage_num - 1)
if __name__ == '__main__':
    main(sys.argv)
