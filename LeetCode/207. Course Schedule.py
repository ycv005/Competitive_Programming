from collections import defaultdict

# DFS approach, on exploring each node, checking its presence
# inside visited and exploring_nodes. If the node is
# present inside them, mean we found a cycle.


class Solution:
    def __init__(self):
        self.edge = defaultdict(list)

    def isCycle(self, node, visited, exploring_nodes):
        # node is visited
        visited[node] = True
        # node is currently being explored
        exploring_nodes[node] = True
        # exploring its neighbour
        for neighbour in self.edge[node]:
            if visited[neighbour] == False:
                if self.isCycle(neighbour, visited, exploring_nodes):
                    return True
            elif exploring_nodes[neighbour]: # means visited[node] = True
                return True
        # node is explored
        exploring_nodes[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = {}
        for des, src in prerequisites:
            visited[src] = visited[des] = False
            self.edge[src].append(des)

        # dict = dict, it makes a deep copy, pointing to same, instead using .copy()
        exploring_nodes = visited.copy()
        hasCycle = False
        # exploring each node, (visited contains all node)
        for node in visited.keys():
            if visited[node] == False and self.isCycle(node, visited, exploring_nodes):
                hasCycle = True
                break

        # if cycle, not possible
        return not hasCycle
