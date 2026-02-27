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

# 

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

# BFS(**Breath First Search**)

思路：

1访问当前节点，并将该节点标记为被访问

2将该节点加入到队列中

3从队列的首位获取节点

4按照某种方法或者顺序获取该节点的邻接点，加入到队列中

5重复3,4,直至完成目标或对列为空
