import copy
import operator

# to do : answer depth in bfs , paths in all of them


class Node:
    instances = []

    def __init__(self, lst):
        self.path = ''
        self.lst = lst
        self.totalNum = 0
        self.depth = 0
        self.node_path = []
        Node.instances.append(self)

    def get_path(self):
        return self.path

    def set_path(self, p):
        self.path = p

    def get_list(self):
        return self.lst

    def get_num(self):
        return self.totalNum

    def set_num(self, num):
        self.totalNum = num


class Card:
    def __init__(self, string):
        color = string[-1]
        string = string[:-1]
        number = int(string)
        self.color = color
        self.number = number

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.number == other.number and self.color == other.color


def get_input(num):
    decks1 = [[] for j in range(num)]
    for i in range(num):
        ele = input()
        temp = ele.split()
        for card in temp:
            if card == '#':
                decks1[i] = []
            else:
                decks1[i].append(Card(card))

    return decks1


def child_node(lst):
    child_nodes = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            list_copy = copy.deepcopy(lst)
            decks_list1 = lst[i]
            decks_list2 = lst[j]
            if i != j:
                if len(decks_list1) != 0 and len(decks_list2) != 0:
                    if decks_list1[len(decks_list1) - 1].number < decks_list2[len(decks_list2) - 1].number:
                        path = "card " + str(decks_list1[len(decks_list1) - 1].number) + str(decks_list1[len(decks_list1) - 1].color)+" move from deck "+str(i)+" to deck "+str(j)
                        list_copy[i].pop(len(decks_list1) - 1)
                        list_copy[j].append(decks_list1[len(decks_list1) - 1])
                        child_nodes.append(list_copy)
                        # path_list.set_path(path)
                        # path_list.node_path = copy.deepcopy(path_list.node_path)
                        # path_list.node_path.append(path_list.get_path())

                if len(decks_list2) == 0 and len(decks_list1) != 0:
                    path = "card " + str(decks_list1[len(decks_list1) - 1].number) + str(decks_list1[len(decks_list1) - 1].color)+" move from deck "+str(i)+" to deck "+str(j)
                    # path_list.append(path)
                    list_copy[i].pop(len(decks_list1) - 1)
                    list_copy[j].append(decks_list1[len(decks_list1) - 1])
                    child_nodes.append(list_copy)
                    # path_list.set_path(path)
                    # path_list.node_path = copy.deepcopy(path_list.node_path)
                    # path_list.node_path.append(path_list.get_path())
    return child_nodes


def print_decks(lst):
    for c in range(k):
        if len(lst[c]) == 0:
            print('#', end='')
        for obj in lst[c]:
            print(str(obj.number)+str(obj.color), end=" ")
        print()


def is_sorted(lst):
    reverse_sort = copy.deepcopy(lst)
    for i in range(len(reverse_sort)):
        reverse_sort.append(reverse_sort[i].sort(key=operator.attrgetter('number'), reverse=True))
    if all(x in reverse_sort for x in lst):
        return True
    return False


def same_color(lst):  # lst is first child
    for i in range(len(lst)):
        if len(lst[i]) != 0:
            color = lst[i][0].color
            for obj in lst[i]:
                if str(obj.color) != str(color):
                    return False
    return True


def same_size(lst, the_len):
    it = iter(lst)
    if all(len(l) == the_len or len(l) == 0 for l in it):
        return True
    return False


def is_goal(main_lst, the_len):
    for i in range(len(main_lst)):
        for j in range(k):
            if is_sorted(main_lst[i]) and same_size(main_lst[i], the_len) and same_color(main_lst[i]) :
                # print(*path_list.node_path , sep="\n")
                print_decks(main_lst[i])
                return True
    return False
# and same_size(main_lst[i], the_len)


def goal_check(main_lst, the_len):
    for i in range(len(main_lst)):
        for j in range(k):
            if is_sorted(main_lst[i]) and same_size(main_lst[i], the_len) and same_color(main_lst[i]) :
                return True
    return False
# and same_size(main_lst[i], the_len)


expand_node = 0
generate_node = 1


def bfs(start , the_len):   # start is child_deck[i] it mean first child
    global expand_node
    global generate_node
    # global depth
    frontier = [start]                 # main lst is every child of a node
    explored = []
    goal = False
    while not goal:
        expand_node += 1
        if not frontier :
            print("No answer")
            return False
        cur_node = frontier.pop(0)
        explored.append(cur_node)
        children = child_node(cur_node)
        # depth += 1

        for child in children:
            if child not in frontier and child not in explored:
                generate_node += 1
                frontier.append(child)
        if is_goal(explored , the_len):
            goal = True
            print("GOAL!")


if __name__ == '__main__':
    inp = input()
    k = int(inp[0])  # number of decks
    m = int(inp[2])  # number of colors , m should be less than k
    n = int(inp[4])  # number of numbers from 1 to n
    decks = get_input(k)
    bfs(decks, n)
    # print("Answer depth :" , depth)
    print("Generated nodes : " ,  generate_node)
    print("Expanded nodes : " , expand_node)
