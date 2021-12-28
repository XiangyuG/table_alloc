import sys
import random


def main(argv):
    if len(argv) != 2:
        print("Usage: python3 " + argv[1] + " <number of tables>")
        sys.exit(1)
    out_str = ""
    num = int(argv[1])
    table_list = []
    for i in range(num):
        table_list.append("T" + str(i))
    print(table_list)
    for i in range(num):
        for j in range(i + 1, num):
            if random.random() > 0.5:
                out_str += table_list[i] + " " + table_list[j] + "\n"
    print(out_str)


if __name__ == '__main__':
    main(sys.argv)
