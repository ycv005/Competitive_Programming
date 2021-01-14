class Solution:
    def dfs(self, path, res, graph):
        if (len(path) > 0 and path[-1] == len(graph)-1):
            res.append(path)
        else:
            for i, v in enumerate(graph[path[-1]]):
                self.dfs(path + [v], res, graph)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs([0], res, graph)
        return res
