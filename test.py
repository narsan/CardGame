import copy


def printField(people):
    for i in range(0, n):
        print(people[i])


class Node:
    instances = []

    def __init__(self, matrix):
        self.parent = None
        self.matrix = matrix
        self.totalNum = 0
        Node.instances.append(self)

    def getParent(self):
        return self.parent

    def setParent(self, nn):
        self.parent = nn

    def getMatrix(self):
        return self.matrix

    def getNum(self):
        return self.totalNum

    def setNum(self, num):
        self.totalNum = num


def childeNode(tst):
    x = 0
    y = 0
    childeNodes = []
    for i in range(0, n):
        for j in range(0, m):
            if tst[i][j] == "#":
                x = i
                y = j
                break
    if x - 1 >= 0:
        a = copy.deepcopy(tst)
        tmp = a[x][y]
        a[x][y] = a[x - 1][y]
        a[x - 1][y] = tmp
        childeNodes.append(a)
    if x + 1 < n:
        a = copy.deepcopy(tst)
        tmp = a[x][y]
        a[x][y] = a[x + 1][y]
        a[x + 1][y] = tmp
        childeNodes.append(a)
    if y - 1 >= 0:
        a = copy.deepcopy(tst)
        tmp = a[x][y]
        a[x][y] = a[x][y - 1]
        a[x][y - 1] = tmp
        childeNodes.append(a)
    if y + 1 < m:
        a = copy.deepcopy(tst)
        tmp = a[x][y]
        a[x][y] = a[x][y + 1]
        a[x][y + 1] = tmp
        childeNodes.append(a)
    return childeNodes


people = []
inp = input().split()
n = int(inp[0])
m = int(inp[1])
for i in range(0, n):
    inp = input().split()
    people.append(inp)
nn = Node(people)


def goalTest(goalList):
    for i in range(0, n):
        for j in range(0, m):
            if goalList[i][j] == "#":
                y = j
                if (y != 0):
                    return False

    for i in range(0, n):
        if (goalList[i][0] != "#" and m > 1):
            alph = goalList[i][0][3]
            for j in range(1, m):
                if goalList[i][j] != "#" and alph != goalList[i][j][3]:
                    return False
        elif (goalList[i][0] == "#" and m > 1):
            alph = goalList[i][1][3]
            for j in range(2, m):
                if alph != goalList[i][j][3]:
                    return False

    for i in range(0, n):
        for j in range(0, m - 1):
            if (goalList[i][j] != "#"):
                num = int(goalList[i][j][0:3])
                for k in range(j + 1, m):
                    if goalList[i][k] != "#":
                        if num < int(goalList[i][k][0:3]):
                            return False
    return True


def hFunc(node):
    a = node.getMatrix()
    cnt = 0
    for i in range(0, n):
        for j in range(0, m):
            if (a[i][j] == "#"):
                cnt = j
    alph = []
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] != "#" and a[i][j][3] not in alph:
                alph.append(a[i][j][3])

    for i in range(0, n):
        tmp1 = 0
        tmp2 = 0
        for k in range(0, len(alph)):
            for j in range(0, m):
                if a[i][j] != "#" and a[i][j].count(alph[k]):
                    tmp1 = tmp1 + 1
            if tmp2 < tmp1:
                tmp2 = tmp1
            tmp1 = 0
        if tmp2 == m:
            cnt = cnt - 2
        if tmp2 == m - 1:
            cnt = cnt - 1

    tmp3 = 0
    for i in range(0, n):
        for j in range(0, m - 1):
            if (a[i][j] != "#"):
                num = int(a[i][j][0:3])
                for k in range(j + 1, m):
                    if a[i][k] != "#":
                        if num > int(a[i][k][0:3]):
                            tmp3 = tmp3 + 1
        if tmp3 == m:
            cnt = cnt - 1
        elif tmp3 > m / 2:
            cnt = cnt + 1
        elif tmp3 < m / 2:
            cnt = cnt + 2
    return cnt


def gFunc(node):
    cnt = 0
    parent = node.getParent()
    while (True):
        if parent == None:
            break
        else:
            parent = parent.getParent()
            cnt = cnt + 1
    return cnt


expandNode = 0
generatedNode = 1


def aFunc(matrix):
    global expandNode
    global generatedNode
    firstNode = Node(matrix)
    nodeList = [firstNode]

    while (True):
        nodeList.sort(key=lambda x: x.totalNum, reverse=False)

        # for nnn in nodeList:
        #     print(nnn.getNum())
        # print("################")
        nn = nodeList.pop(0)
        expandNode = expandNode + 1
        if goalTest(nn.getMatrix()):
            return nn
        children = childeNode(nn.getMatrix())

        for child in children:
            node = Node(child)
            node.setParent(nn)
            h = hFunc(node)
            g = gFunc(node)
            node.setNum(h + g)
            nodeList.append(node)
            generatedNode = generatedNode + 1


print("Final Ans:")
finalNode = aFunc(people)
printField(finalNode.getMatrix())
print()

print("Expanded Node: " + str(expandNode))
print("Generated Node: " + str(generatedNode))
print()

print("Direction: ")
parent = finalNode.getParent()
directionList = [finalNode, parent]
while True:
    if parent is None:
        break
    else:
        parent = parent.getParent()
        directionList.append(parent)
directionList.reverse()
for tmp in directionList:
    if tmp is None:
        continue
    else:
        printField(tmp.getMatrix())
        print()
