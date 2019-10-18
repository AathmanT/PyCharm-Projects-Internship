def create_graph(parent):
    graph = {}
    for i in range(len(parent)):
        graph[i + 1] = []
    graph[i + 2] = []
    for i in range(len(parent)):
        graph[parent[i]].append(i + 2)
        graph[i + 2].append(parent[i])

    return graph


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def count_red(path, col):
    count = 0
    for i in path:
        if col[i - 1] == 1:
            count = count + 1
    return count


a = [int(j) for j in input().split()]
col = [int(j) for j in input().split()]
par = [int(j) for j in input().split()]

graph = create_graph(par)

l = []
for i in range(a[1]):
    t = [int(j) for j in input().split()]
    l.append(t)

for o in l:
    path = find_path(graph, o[0], o[1], path=[])
    print(count_red(path, col))



