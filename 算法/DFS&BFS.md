# DFS（*Depth First Search*）

## 易错点
### visited标记时机
在标准的深度优先搜索中，
递归开始时（函数开头）打 visited 标记
迭代入栈时打 visited 标记（若有环结构，入栈在标记会存在重复入栈的情况）


思路：

1访问当前节点，并将该节点标记为被访问

2按照某种方法或者顺序获取该节点的邻接点，并遍历

3深入下个节点，如果没被访问，则递归

def DFS(node, graph, visited):



### 模板一：递归版本 (Recursive DFS)

**核心思想**：

1. **访问当前节点**：处理当前节点的逻辑。
2. **标记已访问**：防止重复访问形成无限循环。
3. **递归访问邻居**：对当前节点的每一个未访问的邻居节点，递归调用 DFS。
4. **回溯**：在组合、路径等问题中，递归返回后需要撤销当前的选择（如从路径中移除当前节点），这就是回溯。

**代码模板**：

注意点：

visited 用set





```python
def dfs_recursive(node, graph, visited, path, results):
    """
    递归 DFS 的通用模板函数。

    Args:
        node: 当前正在访问的节点。
        graph: 图的邻接表表示，例如 {'A': ['B', 'C'], ...}。
        visited: 一个集合或布尔数组，用于记录已访问的节点。
        path: 一个列表，用于记录当前的路径（在需要路径的题目中使用）。
        results: 一个列表，用于存储所有找到的结果（如路径、连通分量等）。
    """
    # 1. 终止条件（可选，有时在递归调用前判断）
    # if 某些特定条件（如到达目标节点）:
    #     results.append(path[:]) # 存储结果
    #     return

    # 2. 处理当前节点
    visited.add(node)  # 标记为已访问
    path.append(node)  # 将节点加入当前路径（如果需要记录路径）

    # --- 在这里处理当前节点的业务逻辑 ---
    # 例如：打印节点值、判断是否为目标节点等

    # 3. 递归访问所有邻居节点
    for neighbor in graph.get(node, []):  # 遍历当前节点的所有邻居
        if neighbor not in visited:       # 如果邻居节点未被访问过
            dfs_recursive(neighbor, graph, visited, path, results) # 递归访问它

    # 4. 回溯（如果需要路径，这是关键一步）
    # 在离开当前节点，向上回溯时，撤销对该节点的操作
    path.pop() # 将当前节点从路径中移除

# --- 使用示例 ---
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# visited = set()
# path = []
# results = []
# dfs_recursive('A', graph, visited, path, results)
# print(results) # 输出从 'A' 开始的所有节点组成的连通分量
```

---

### ✅ 模板二：使用栈的迭代版本 (Iterative DFS with Stack)

这个版本手动管理一个栈来模拟系统调用栈，可以避免因递归过深而导致的栈溢出问题。

**核心思想**：

1. **初始化**：将起始节点放入栈中。
2. **循环**：当栈不为空时，弹出栈顶节点。
3. **访问**：如果该节点未被访问过，则处理它并标记为已访问。
4. **扩展**：将其所有未被访问的邻居节点压入栈中。
5. **重复**：重复步骤 2-4，直到栈为空。

**代码模板**：

python

编辑

```python
def dfs_iterative(start_node, graph):
    """
    使用栈实现的迭代 DFS 模板函数。

    Args:
        start_node: DFS 遍历的起始节点。
        graph: 图的邻接表表示，例如 {'A': ['B', 'C'], ...}。
    """
    visited = set()  # 用于记录已访问的节点
    stack = [start_node] # 初始化栈，放入起始节点
    '''
    如果要记录路径，可以修改加入栈的元素结构，如:
    记录path：stack = [ (start_node, [star_node])]，同时在后面的加入栈的过程
    中，把邻节点加入到[]中即可

    '''
    while stack:
        node = stack.pop() # 弹出栈顶节点

        if node not in visited: # 如果该节点未被访问过
            visited.add(node)   # 标记为已访问
            # --- 在这里处理当前节点的业务逻辑 ---
            # 例如：打印 node.val 或 node
            print(node)

            # 将所有未访问的邻居节点压入栈
            # 为了保持与递归版本相同的访问顺序，需要反向添加
            # 因为栈是 LIFO (Last In, First Out)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited # 返回所有访问过的节点集合

# --- 使用示例 ---
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# visited_nodes = dfs_iterative('A', graph)
# print(visited_nodes)
```











# BFS(**Breath First Search**)

思路：

1访问当前节点，并将该节点标记为被访问

2将该节点加入到队列中

3从队列的首位获取节点

4按照某种方法或者顺序获取该节点的邻接点，加入到队列中

5重复3,4,直至完成目标或对列为空
