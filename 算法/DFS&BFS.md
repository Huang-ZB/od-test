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

## 24点游戏

要点：全排列，分治思想

易错点：

1 递归容易使用成使用op ( a , op（ b  , op( c ) ,  op ( d ) )) ，例如求n项和就适用该方法；但本题拥有括号层级的关系，上述方法会导致遗漏op（op（a，b），op（c，d））

递归版本    

```python
import sys

def f(arr:list):
    if len(arr) == 1:
        if abs(arr[0] - 24.0) < 1e-6:
            return True
  
    n = len(arr)
    # 随机取arr中两数计算并把计算结果放回arr中并用新数组保存起来
    # 递归 
    for i in range(n):
        for j in range(n):
            if i != j:
                a = arr[i]
                b = arr[j]

                result = []
                for k in range(n):
                    if k != i and k != j:
                        result.append(arr[k])
              
                result.append(a+b)
                if f(result):
                    return True
                result.pop()

                result.append(a-b)
                if f(result):
                    return True
                result.pop()

                result.append(a*b)
                if f(result):
                    return True
                result.pop()

              
                if b >1e-6:
                    result.append(a/b)
                    if f(result):
                        return True
                    result.pop()
    return False

l = list(map(int,input().split()))

if f(l):
    print("true")
else:
    print("false")
```

迭代版本

```python
import sys

def solve_24_iterative(arr):
    # 使用栈来存储待处理的状态，每个状态是一个数字列表
    stack = [arr]
  
    while stack:
        current_arr = stack.pop()
        n = len(current_arr)
      
        # 终止条件：如果列表中只剩一个数，判断是否接近24
        if n == 1:
            if abs(current_arr[0] - 24.0) < 1e-6:
                return True
            continue
      
        # 遍历所有可能的两数组合 (i, j)
        # 注意：这里 i 和 j 可以互换，因为减法和除法不满足交换律
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
              
                a = current_arr[i]
                b = current_arr[j]
              
                # 构建剩余数字的新列表（排除索引 i 和 j）
                next_arr = []
                for k in range(n):
                    if k != i and k != j:
                        next_arr.append(current_arr[k])
              
                # 尝试四种运算，并将新状态压入栈中
              
                # 1. 加法
                next_arr.append(a + b)
                stack.append(next_arr[:]) # 必须切片复制，否则引用会出错
                next_arr.pop()
              
                # 2. 减法
                next_arr.append(a - b)
                stack.append(next_arr[:])
                next_arr.pop()
              
                # 3. 乘法
                next_arr.append(a * b)
                stack.append(next_arr[:])
                next_arr.pop()
              
                # 4. 除法 (除数不能为0)
                if abs(b) > 1e-6:
                    next_arr.append(a / b)
                    stack.append(next_arr[:])
                    next_arr.pop()
                  
    return False

# 主程序入口
if __name__ == "__main__":
    try:
        # 读取输入，兼容可能的多空格情况
        input_data = sys.stdin.read().strip()
        if not input_data:
            sys.exit(0)
          
        l = list(map(float, input_data.split()))
      
        # 确保输入是4个数（虽然原题逻辑对任意长度有效，但24点通常是4个）
        if len(l) < 1:
            print("false")
        else:
            if solve_24_iterative(l):
                print("true")
            else:
                print("false")
    except Exception:
        print("false")
```

# 针对多叉决策树（Multi-way Decision Tree）的遍历

核心在于处理每个节点可能有 $N$ 个子节点的情况。与二叉树不同，多叉树通常使用列表或数组来存储子节点。

以下是带有**路径保存**（记录从根节点到当前节点的路径）的 DFS 模板，包含递归和迭代两种实现方式。

### 1. 数据结构定义
首先定义一个通用的多叉树节点类。

```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        # children 是一个 Node 对象的列表
        self.children = children if children is not None else []
```

---

### 2. 递归实现 (Recursive DFS)
递归写法最直观。我们需要维护一个 `path` 列表，在进入节点时将其加入路径，在回溯（返回上一层）时将其移除。

```python
def dfs_recursive(root, target_condition=None):
    """
    多叉树 DFS 递归模板 (带路径保存)
    
    :param root: 根节点
    :param target_condition: 可选，一个函数，用于判断当前路径是否满足条件 (例如找到目标值)
    :return: 所有满足条件的路径列表，若无条件则返回所有路径
    """
    results = []
    
    def backtrack(node, current_path):
        if not node:
            return

        # 1. 做选择：将当前节点加入路径
        current_path.append(node.val)
        
        # 2. 检查是否满足终止条件或收集结果
        # 如果没有特定条件，通常在这里收集所有完整路径（如果是叶子节点）或所有路径
        if not node.children: 
            # 如果是叶子节点，保存当前路径的拷贝
            results.append(list(current_path))
        elif target_condition and target_condition(current_path):
            # 如果定义了条件且满足，也可以保存（视具体题目要求，是找叶子还是找中间节点）
            results.append(list(current_path))
        
        # 3. 遍历所有子节点 (多叉的核心)
        for child in node.children:
            backtrack(child, current_path)
            
        # 4. 撤销选择：回溯，移除当前节点
        current_path.pop()

    if not root:
        return []
        
    backtrack(root, [])
    return results
```

#### 使用示例
```python
# 构建一个简单的多叉树
#       A
#     / | \
#    B  C  D
#      / \
#     E   F
root = Node('A', [
    Node('B'),
    Node('C', [Node('E'), Node('F')]),
    Node('D')
])

# 获取所有从根到叶子的路径
all_paths = dfs_recursive(root)
print("所有路径:", all_paths)
# 输出: [['A', 'B'], ['A', 'C', 'E'], ['A', 'C', 'F'], ['A', 'D']]
```

---

### 3. 迭代实现 (Iterative DFS)
迭代写法需要使用显式的**栈 (Stack)**。
**关键点**：为了在迭代中保存路径，栈中存储的元素不仅仅是节点，而是 `(节点, 当前路径)` 的元组。或者，我们可以模拟递归栈的行为，但直接存储路径副本通常代码更简洁，虽然空间复杂度稍高。

#### 方法 A：栈中存储路径副本（代码最简洁，推荐）
这种方法逻辑清晰，每次压栈时都创建一个新的路径列表。

```python
def dfs_iterative(root, target_condition=None):
    """
    多叉树 DFS 迭代模板 (带路径保存)
    使用栈存储 (节点, 当前路径)
    """
    if not root:
        return []
    
    results = []
    # 栈元素: (当前节点, 到达该节点的路径列表)
    stack = [(root, [root.val])]
    
    while stack:
        node, path = stack.pop()
        
        # 检查是否满足条件或是否为叶子节点
        if not node.children:
            results.append(path)
        elif target_condition and target_condition(path):
            results.append(path)
            
        # 将子节点压入栈
        # 注意：如果需要保持从左到右的遍历顺序，需要逆序压栈
        # 因为栈是 LIFO (后进先出)
        for child in reversed(node.children):
            # 创建新路径列表，避免引用污染
            new_path = path + [child.val]
            stack.append((child, new_path))
            
    return results
```

#### 方法 B：优化空间（仅当路径极长且内存敏感时使用）
如果树非常深，复制路径列表可能会消耗大量内存。此时可以像递归一样，维护一个全局 `path` 列表，并在栈中记录“状态”以便回溯。但这在多叉树迭代中实现较复杂（需要记录子节点遍历到的索引），通常**方法 A** 在算法竞赛和面试中更为通用且不易出错。

---

### 4. 关键差异与注意事项

| 特性 | 递归 (Recursive) | 迭代 (Iterative) |
| :--- | :--- | :--- |
| **路径维护** | 利用函数调用栈隐式维护，通过 `append` 和 `pop` 回溯。 | 显式将路径列表作为状态存入栈中 (`stack.append((node, path))`)。 |
| **子节点遍历** | `for child in node.children:` 自然顺序。 | 若需保持自然顺序，需 `reversed(node.children)` 压栈。 |
| **空间复杂度** | $O(H)$ (H为树高)，路径列表复用。 | $O(N \times H)$ (最坏情况)，因为每个栈帧都持有一个路径副本。 |
| **适用场景** | 树深度适中，代码可读性优先。 | 树深度极大（防止递归栈溢出），或需要精细控制遍历过程。 |

### 5. 常见变体：寻找特定目标
如果在决策树中寻找满足特定条件的路径（例如：路径和等于 Target），只需修改 `target_condition` 或在循环内部增加判断：

```python
# 示例：寻找路径和等于 target_sum 的路径 (假设节点值为数字)
def find_paths_with_sum(root, target_sum):
    def check_sum(path):
        return sum(path) == target_sum
    
    # 复用上面的模板，只收集叶子节点且满足和的路径
    # 注意：这里需要微调逻辑，通常是在叶子节点判断
    results = []
    stack = [(root, [root.val])]
    
    while stack:
        node, path = stack.pop()
        
        if not node.children: # 叶子节点
            if sum(path) == target_sum:
                results.append(path)
        
        for child in reversed(node.children):
            stack.append((child, path + [child.val]))
            
    return results
```

这两个模板可以直接应用于 LeetCode 上的多叉树问题（如 N 叉树的最大深度、路径总和等）以及各类决策树搜索问题。

# BFS(**Breath First Search**)

思路：

1访问当前节点，并将该节点标记为被访问

2将该节点加入到队列中

3从队列的首位获取节点

4按照某种方法或者顺序获取该节点的邻接点，标记访问，加入到队列中

5重复3,4,直至完成目标或对列为空



## Dijkstra
带权图 (边权重  >= 0 )
Dijkstra 算法 = BFS 的广度优先思想 + 最小堆优化（加速选点过程+贪心策略（每次选当前最近的））


| 特性 | BFS (广度优先搜索) | Dijkstra (戴克斯特拉) |
| :--- | :--- | :--- |
| 适用场景 | 无权图 (或所有边权重相等，如都是1) | 带权图 (边权重  $ \ge 0 $ ，且各不相同) |
| 数据结构 | 普通队列 (FIFO - 先进先出) | 优先队列/最小堆 (按距离排序) |
| 出队逻辑 | 谁先进入队列，谁就先出来。 | 谁当前的累积距离 (`dist`) 最小，谁就先出来。 |
| 正确性保证 | 因为边权相等，第一次访问到某点时，路径一定是最短的。 | 因为使用了贪心策略，只有当从堆中弹出某点时，才确定找到了它的最短路径。 |





### 模板

1.  **核心逻辑冗余与错误：距离更新时机**
    *   **问题**：代码中先判断 `if distance < get_distance...` 然后 `change_distance`，接着 `else: continue`。
    *   **标准做法**：Dijkstra 的标准优化是**出堆时检查**。如果 `distance > min_grids[node]`，说明该节点已经被更短的路径访问过了，直接 `continue`。**不需要**在出堆后再次更新 `min_grids[node]`，因为入堆时的值一定大于等于当前记录的最短值（除非是第一次访问）。
    *   **后果**：原逻辑虽然不一定错，但非常啰嗦且容易出错。标准的写法是：如果当前取出的距离比记录的大，直接跳过。

2.  **剪枝逻辑缺失**
    *   **问题**：在将邻居加入堆之前，没有严格检查 `cur_distance < min_grids[neighbor]` 后再入堆（虽然代码里写了，但结合上面的逻辑混乱，容易失效）。
    *   **优化**：必须在入堆前确认新路径更短，否则堆会无限膨胀，导致超时（TLE）。

3.  **变量命名拼写**
    *   `neibor` -> `neighbor`
    *   `min_girds` -> `min_grids` (虽然不影响运行，但建议规范)

---
### ✅ 优化后的标准模板 (Python)

这是一个修复了所有逻辑错误、符合 Python 规范且效率最高的 Dijkstra 模板。假设网格/图的权重非负。

```python
import heapq
from typing import List, Tuple, Dict, Any

# 假设 grids 是某种结构，这里用通用逻辑演示
# 如果 grids 是二维数组，node 通常是 (r, c) 元组
# distance_func 用于获取两点间的权重

def dijkstra(grids: Any, start: Tuple, start_distance: int, target: Tuple) -> int:
    """
    grids: 图的数据结构
    start: 起点坐标/ID
    start_distance: 起始距离 (通常为 0)
    target: 终点坐标/ID
    """
    
    # 1. 初始化距离字典或矩阵
    # 使用字典可以处理稀疏图或非整数坐标，如果是密集矩阵可用 [[inf]*w for _ in range(h)]
    min_distances = {} 
    # 或者如果是已知大小的矩阵: min_distances = [[float('inf')] * cols for _ in range(rows)]
    
    # 初始化起点
    min_distances[start] = start_distance
    
    # 2. 优先队列 (距离, 节点)
    # Python 的 heapq 是最小堆
    pq = [(start_distance, start)]
    
    while pq:
        cur_dist, node = heapq.heappop(pq)
        
        # 3. 剪枝 (关键优化)
        # 如果当前取出的距离 大于 记录的最短距离，说明这是旧的路径，直接跳过
        if cur_dist > min_distances.get(node, float('inf')):
            continue
        
        # 4. 提前终止 (可选优化)
        # 由于算法的特性，每次都是取路径最小的进行处理，每次取出的一定是源点到底达当前点的最短路径。所以第一次弹出目标节点时，其距离必然是最小的
        if node == target:
            return cur_dist
        
        # 5. 遍历邻居
        # 需要用户实现 get_neighbors 和 get_weight 函数
        for neighbor in get_neighbors(grids, node):
            weight = get_weight(grids, node, neighbor)
            new_dist = cur_dist + weight
            
            # 6. 松弛操作 (Relaxation)
            # 只有当发现更短路径时，才更新并加入堆
            if new_dist < min_distances.get(neighbor, float('inf')):
                min_distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    # 7. 如果循环结束还没返回，说明无法到达目标
    return min_distances.get(target, float('inf'))

# --- 辅助函数示例 (需要根据具体题目实现) ---

def get_neighbors(grids, node):
    """
    返回 node 的所有邻居节点列表
    例如在网格中返回上下左右合法的坐标
    """
    r, c = node
    rows, cols = len(grids), len(grids[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            # 假设 grids[nr][nc] != 1 表示不是障碍物
            if grids[nr][nc] != 1: 
                neighbors.append((nr, nc))
    return neighbors

def get_weight(grids, node, neighbor):
    """
    返回从 node 到 neighbor 的权重
    如果是无权图，返回 1
    如果是带权图，返回 grids[neighbor[0]][neighbor[1]] 或其他逻辑
    """
    # 示例：假设网格值代表通过该点的代价
    return grids[neighbor[0]][neighbor[1]]
```

### 💡 关键修改点总结

1.  **修复 `heapq` 调用**：改为 `heapq.heappop(pq)` 和 `heapq.heappush(pq, item)`。
2.  **修正剪枝逻辑**：
    *   **出堆时**：`if cur_dist > min_distances[node]: continue`。这是防止重复计算的关键。
    *   **入堆前**：`if new_dist < min_distances[neighbor]`。这能显著减少堆的大小，提高性能。
3.  **移除错误的更新**：去掉了原代码中出堆后尝试 `change_distance` 的逻辑，因为如果能通过剪枝检查，说明 `cur_dist` 就是当前的 `min_distances[node]`，无需再次赋值。

4.  **处理不可达情况**：如果队列空了还没找到 target，返回 `float('inf')` 而不是报错或未定义行为。

### 针对网格题的特别提示
如果你是在做 LeetCode 或类似的网格最短路径题：
*   **初始化**：通常用 `dist = [[float('inf')] * n for _ in range(m)]` 比字典更快。
*   **方向数组**：预先定义 `dirs = [(0,1), (0,-1), (1,0), (-1,0)]`。
*   **边界检查**：在 `get_neighbors` 中务必检查 `0 <= x < m` 和 `0 <= y < n` 以及障碍物。

这个优化后的模板可以直接用于绝大多数最短路径场景。