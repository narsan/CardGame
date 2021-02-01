import re
import copy
import operator


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.number == other.number and self.color == other.color


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def get_input(num):
    decks1 = [[] for j in range(num)]
    for i in range(num):
        ele = input()
        temp = re.findall('\d+|\D+', ele)
        for x, y in pairwise(temp):
            decks1[i].append(Card(x, y))

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
                        list_copy[j].append(Card(decks_list1[len(decks_list1) - 1].number,
                                                 decks_list1[len(decks_list1) - 1].color))
                        child_nodes.append(list_copy)

                if len(decks_list2) == 0 and len(decks_list1) != 0:
                    # print("list copy i" , list_copy[i])
                    list_copy[i].pop(len(decks_list1) - 1)
                    list_copy[j].append(Card(decks_list1[len(decks_list1) - 1].number,
                                             decks_list1[len(decks_list1) - 1].color))
                    child_nodes.append(list_copy)

    return child_nodes


def bfs(start , the_len):   # start is child_deck[i] it mean first child
    print("in BFS")
    frontier = [start]                 # main lst is every child of a node
    explored = []
    goal = False
    while not goal:
        if not frontier :
            print("No answer looser")
            return False
        cur_node = frontier.pop(0)
        explored.append(cur_node)
        children = child_node(cur_node)
        for child in children:
            if child not in frontier and child not in explored:
                frontier.append(child)
                print("-----------------")
                for b in range(len(frontier)):
                    for c in range(k):
                        if len(frontier[b][c]) == 0:
                            print('#')
                        for obj in frontier[b][c]:
                            print(obj.number, obj.color, end=" ")
                        print()
                    print()

        if is_goal(explored , the_len):
            print("here")
            goal = True
            print("GOAL!")
        # explored.append(next())


def is_sorted(lst):
    reverse_sort = copy.deepcopy(lst)
    for i in range(len(reverse_sort)):
        reverse_sort.append(reverse_sort[i].sort(key=operator.attrgetter('number'), reverse=True))
    if all(x in reverse_sort for x in lst):
        print('sorted')
        return True
    return False


def same_color(lst):
    if len(lst) != 0:
        color = lst[0].color.strip()
        for obj in lst:
            if obj.color.strip() != color:
                return False
        print("color ok")
        return True

    # flag = False
    # if len(lst) != 0:
    #     color = lst[0].color
    #     print("main color" , color)
    #     for obj in lst:
    #         print("color" , obj.color)
    #         if obj.color == color :
    #             flag = True
    #
    #     if flag :
    #         print("color ok")
    #         return True
    #     return False


def same_size(lst, the_len):
    print("asn miai inja")
    it = iter(lst)
    if all(len(l) == the_len or len(l) == 0 for l in it):
        print("size ok")
        return True
    return False
    # for deck in lst:
    #     if len(deck) != 3 or len(deck) != 0:
    #         return False
    # print("size ok")
    # return True


def is_goal(main_lst, the_len):
    print("in is goal")
    for i in range(len(main_lst)):
        for j in range(k):
            if is_sorted(main_lst[i]) and same_size(main_lst[i], the_len) and same_color(main_lst[i][j]) :
                print("**********************")
                for c in range(k):
                    if len(main_lst[i][c]) == 0:
                        print('#', end='')
                    for obj in main_lst[i][c]:
                        print(obj.number, obj.color, end=" ")
                    print()
                return True
    return False


if __name__ == '__main__':
    inp = input()
    k = int(inp[0])  # number of decks
    m = int(inp[2])  # number of colors , m should be less than k
    n = int(inp[4])  # number of numbers from 1 to n
    decks = get_input(k)
    index1 = []
    index2 = []
    test_list = []
    # decks_children = child_node(decks)
    bfs(decks , n)

    #
    # if not (is_goal(decks_children, n)):
    #     # while not is_goal(test_list , n):
    #         for i in range(decks_children.__len__()):
    #             print('child' , i)
    #             test_list = child_node(decks_children[i])
    #             print("len", test_list.__len__())
    #             for b in range(test_list.__len__()):
    #                 for c in range(k):
    #                     if test_list[b][c].__len__() == 0:
    #                         print('#')
    #                     for obj in test_list[b][c]:
    #                         print(obj.number, obj.color, end=" ")
    #                     print()
    #                 print()

    # for b in range(decks_children.__len__()):
    #     for c in range(k):
    #         if decks_children[b][c].__len__() == 0:
    #             print('#')
    #         for obj in decks_children[b][c]:
    #             print(obj.number, obj.color, end=" ")
    #         print()
    #     print()

# 3 3 3
# 3r 2r 1r
# 3b 2b
# 1b
# 3 3 3
# 3r 2r 1r
# 3b 2b 1b
# #

#


# 3
# 3
# 3
# 1r 3r 2r
# 1b 2b 3b
# 1y 2y 4y

# 5 3 5
# 5g 5r 4y
# 2g 4r 3y 3g 2y
# 1y 4g 1r
# 1g 2r 5y 3r
# #


# 5 3 5
# 5y 4y 3y 2y 1y
# 1g
# 1r
# 5r 4r 3r 2r
# 5g 4g 3g 2g