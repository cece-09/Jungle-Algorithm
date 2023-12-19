class Solution(object):
    def calcEquation(self, equations, values, queries):
        inf = float('inf')

        # Do dfs
        def dfs(graph, src, des, visit, result):
            # If destination is found           
            if graph[src][des] != inf:
                return result * graph[src][des]
            
            n = len(visit)
            rtn = inf
            for i in range(n):
                if not visit[i] and graph[src][i] != inf:
                    visit[i] = 1
                    rtn = min(rtn, dfs(graph, i, des, visit, result * graph[src][i]))
                
            return rtn
            
        
        # Parse the equations first
        idx = 0
        nodes = {}
        for a, b in equations:
            if a not in nodes:
                nodes[a] = idx
                idx += 1
            if b not in nodes:
                nodes[b] = idx
                idx += 1
        
        # Graph as adjacency matrix
        n, m = len(nodes), len(equations)
        graph = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            # Division between same num is 1
            graph[i][i] = 1

        for k in range(m):
            v = values[k]
            a, b = equations[k]
            i, j = nodes[a], nodes[b]
            graph[i][j] = v
            graph[j][i] = 1 / float(v)

        # find the sum of costs in path
        answer = []
        for query in queries:
            a, b = query
            if not (a in nodes and b in nodes):
                # if not a valid variable
                answer.append(-1)
                continue

            src, des = nodes[a], nodes[b]
            visit = [0 for _ in range(n)]
            result = dfs(graph, src, des, visit, 1)
            if result == inf:
                answer.append(-1)
                continue
            answer.append(result)
        
        return answer

        

sol = Solution()
# sol.calcEquation([["a","e"],["b","e"]], [4.0,3.0], [["a","b"],["e","e"],["x","x"]])
# sol.calcEquation([["a","b"],["b","c"]], [2.0, 3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
# sol.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
# sol.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
# sol.calcEquation([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]])
sol.calcEquation([["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]], [2.0,3.0,4.0,5.0,6.0,7.0,8.0], [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]])