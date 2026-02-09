def DFS(node, graph, visited:set, target):
    # 加入visited，标记为被访问
    visited.add(node)
    # 递归版本DFS
    #  终止条件
    #  如常见的：节点等于目标点，或满足自定义的条件
    if node ==target:
        ......
    

    for next_node in graph.get_next(node):
        # 遍历邻接点,先标记访问，在递归
        DFS(next_node,.......)



def DFS(start_node, graph, visited, stack_DFS, target):
    # 初始化栈和visited
    stack_DFS = [start_node]
    visited = set()

    while stack_DFS:  
        cur_node = stack_DFS.pop() # 弹出节点
       
        if cur_node not in visited:  # 判断是否访问过
            visited.add(cur_node)

            # 业务判断，如找到目标点
            if cur_node == target:
                ......
            
            # 将所有未访问的邻居节点压入栈
            # 为了保持与递归版本相同的访问顺序，需要反向添加
            # 因为栈是 LIFO (Last In, First Out)
            for next_node in graph.get_next(node,[]):
                if cur_node not in visited:
                    visited.append(node)
                    stack_DFS.append(next_node)

