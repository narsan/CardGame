import copy
import operator


class Node:
    instances = []

    def __init__(self, lst):
        self.parent = None
        self.lst = lst
        self.totalNum = 0
        self.depth = 0
        Node.instances.append(self)

    def get_parent(self):
        return self.parent

    def set_parent(self, nn):
        self.parent = nn

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
                        list_copy[i].pop(len(decks_list1) - 1)
                        list_copy[j].append(decks_list1[len(decks_list1) - 1])
                        child_nodes.append(list_copy)

                if len(decks_list2) == 0 and len(decks_list1) != 0:
                    list_copy[i].pop(len(decks_list1) - 1)
                    list_copy[j].append(decks_list1[len(decks_list1) - 1])
                    child_nodes.append(list_copy)
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
            if is_sorted(main_lst[i]) and same_size(main_lst[i], the_len) and same_color(main_lst[i]):
                print_decks(main_lst[i])
                print("GOAL!")
                return True
    return False


def function_g(node):
    cnt = 0
    parent = node.get_parent()
    while True:
        if parent is None:
            break
        else:
            parent = parent.get_parent()
            cnt = cnt + 1
    return cnt


def function_h(node):  # node is child in children
    child = node.get_list()
    cnt = 0
    for i in range(len(child)):
        if len(child[i]) != 0:
            if child[i][0].number != n:
                cnt += len(child[i])
            else:
                for j in range(len(child[i])):
                    if child[i][0].color != child[i][j].color:
                        cnt += 1
                    elif i != j and child[i][j].number < child[i][j].number:
                        cnt += 1
    return cnt


expand_node = 0
generate_node = 1


def a_star(lst , the_len):
    global expand_node
    global generate_node
    start = Node(lst)
    frontier = [start]
    explored = []
    g = 0
    while True:
        frontier.sort(key=lambda x: x.totalNum)
        cur_node = frontier.pop(0)
        expand_node += 1
        explored.append(cur_node.get_list())
        if is_goal(explored , the_len):
            print("Answer depth " , g)
            return True
        children = child_node(cur_node.get_list())
        for child in children:
            node = Node(child)
            node.set_parent(cur_node)
            h = function_h(node)
            g = function_g(node)
            node.set_num(h + g)
            frontier.append(node)
            generate_node += 1


if __name__ == '__main__':
    inp = input()
    k = int(inp[0])  # number of decks
    m = int(inp[2])  # number of colors , m should be less than k
    n = int(inp[4])  # number of numbers from 1 to n
    decks = get_input(k)
    a_star(decks , n)
    print("Expanded Node: " + str(expand_node))
    print("Generated Node: " + str(generate_node))
    # children = child_node(decks)
    # for c in range(k):
    #     if len(children[0][0]) == 0:
    #         print('#', end='')
    #     for obj in children[0][c]:
    #         print(obj.number, obj.color, end=" ")
    #     print()
    #
    # function_h(Node(children[0]))

    # node1 = Node(decks)
    # nn = Node(decks)
    # for child in children:
    #     node1 = Node(child)
    #     node1.set_parent(nn)
    #     g = function_g(node1)
    #     print("g = " , g)
    # g = function_g(node1)
    # print(node1.get_list()[0][0].number)
