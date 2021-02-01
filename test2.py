import re
import copy
import operator


class Node:
    instances = []

    def __init__(self, lst):
        self.parent = None
        self.path = ''
        self.lst = lst
        self.totalNum = 0
        self.depth = 0
        self.node_path = []
        Node.instances.append(self)
        self.depth = 0

    def get_parent(self):
        return self.parent

    def set_parent(self, nn):
        self.parent = nn

    def get_path(self):
        return self.path

    def set_path(self, p):
        self.path = p

    def get_list(self):
        return self.lst

    # def set_list(self , lst):
    #     self.lst = lst

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
    # lst = Node(lst)
    child_nodes = []
    child_nodes = Node(child_nodes)
    for i in range(len(lst.get_list())):
        for j in range(len(lst.get_list())):
            list_copy = copy.deepcopy(lst.get_list())
            decks_list1 = lst.get_list()[i]
            decks_list2 = lst.get_list()[j]
            if i != j:
                if len(decks_list1) != 0 and len(decks_list2) != 0:
                    if decks_list1[len(decks_list1) - 1].number < decks_list2[len(decks_list2) - 1].number:
                        new_node = Node(list_copy)
                        path = "card " + str(decks_list1[len(decks_list1) - 1].number) + str(decks_list1[len(decks_list1) - 1].color)+" move from deck "+str(i)+" to deck "+str(j)
                        list_copy[i].pop(len(decks_list1) - 1)
                        list_copy[j].append(decks_list1[len(decks_list1) - 1])
                        child_nodes.get_list().append(list_copy)
                        new_node.set_path(path)
                        # new_node.node_path = copy.deepcopy(lst.node_path)
                        new_node.node_path.append(new_node.get_path())
                        # print("attempt failed" , new_node.node_path)
                        # print(len(new_node.node_path))
                        new_node.depth = new_node.depth + 1
                        new_node.set_parent(lst)
                        if goal_check(new_node , n):
                            print("here")
                            print("emmm" , new_node.node_path)
                            print(new_node.depth)

                if len(decks_list2) == 0 and len(decks_list1) != 0:
                    new_node = Node(list_copy)
                    path = "card " + str(decks_list1[len(decks_list1) - 1].number) + str(decks_list1[len(decks_list1) - 1].color) + " move from deck " + str(i) + " to deck " + str(j)
                    list_copy[i].pop(len(decks_list1) - 1)
                    list_copy[j].append(decks_list1[len(decks_list1) - 1])
                    child_nodes.get_list().append(list_copy)
                    new_node.set_path(path)
                    # new_node.node_path = copy.deepcopy(lst.node_path)
                    new_node.node_path.append(new_node.get_path())
                    new_node.depth = lst.depth + 1
                    new_node.set_parent(lst)
                    if goal_check(new_node, n):
                        print("here2")
                        print("ooom" , new_node.node_path)

    return child_nodes


def print_decks(lst):
    for c in range(k):
        if len(lst[c]) == 0:
            print('#', end='')
        for obj in lst[c]:
            print(obj.number, obj.color, end=" ")
        print()


def is_sorted(lst):
    reverse_sort = copy.deepcopy(lst)
    for i in range(len(reverse_sort)):
        reverse_sort.append(reverse_sort[i].sort(key=operator.attrgetter('number'), reverse=True))
    if all(x in reverse_sort for x in lst):
        return True
    return False


def same_color(lst):                # lst is first child
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


def goal_check(main_lst, the_len):
    # for i in range(len(main_lst.get_list())):
    #     for j in range(k):
    if is_sorted(main_lst.get_list()) and same_size(main_lst.get_list(), the_len) and same_color(main_lst.get_list()) :
        return True
    return False


def is_goal(main_lst, the_len):
    for i in range(len(main_lst)):
        for j in range(k):
            if is_sorted(main_lst[i].get_list()) and same_size(main_lst[i].get_list(), the_len) and same_color(main_lst[i].get_list()) :
                print_decks(main_lst[i])
                return True
    return False


def bfs(lst , the_len):   # start is child_deck[i] it mean first child
    expand_node = 0
    generate_node = 1
    start = Node(lst)
    frontier = [start]                 # main lst is every child of a node
    explored = []
    goal = False
    while not goal:
        expand_node += 1
        if not frontier :
            print("No answer looser")
            return False
        print(frontier[0])
        cur_node = frontier.pop(0)
        print("!!" , type(cur_node))
        explored.append(cur_node)
        children = child_node(cur_node)
        for child in children.get_list():
            if child not in frontier and child not in explored:
                generate_node += 1
                frontier.append(child)
        if is_goal(explored , the_len):
            goal = True
            print("GOAL!")
            print("Generated nodes : " ,  generate_node)
            print("Expanded nodes : " , expand_node)


def dls(start , limit , the_len):
    expand_node = 0
    expand_node += 1
    generate_node = 1
    frontier = [start]
    explored = []
    cur_node = frontier.pop(0)
    explored.append(cur_node)
    if is_goal(explored , the_len):
        print("GOAL!")
        print("Generated nodes : " ,  generate_node)
        print("Expanded nodes : " , expand_node)
        return True
    elif limit <= 0:
        return False
    else:
        children = child_node(cur_node)
        generate_node += len(children)
        for child in children:
            if dls(child, limit - 1 , the_len):
                return True
        return False


def ids(start , limit , the_len):

    for i in range(limit):
        print("Limit is :" , i)
        if dls(start , i , the_len):
            return True
    return False


if __name__ == '__main__':
    ids_limit = 3
    inp = input()
    k = int(inp[0])  # number of decks
    m = int(inp[2])  # number of colors , m should be less than k
    n = int(inp[4])  # number of numbers from 1 to n
    decks = get_input(k)
    print("Path: ")
    print()
    bfs(decks, n)

# 5 3 5
# 5y 4y 3y 2y 1y
# #
# #
# 5r 4r 3r 2r 1g
# 5g 4g 3g 2g 1r