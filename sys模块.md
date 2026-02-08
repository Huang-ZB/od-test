# sys 模块

1 sys.stdin 标准输入

```python
import sys
# 一次性读取所有输入
lines = sys.stdin.read()

# 一次性读取所有输入并按行分割,含有换行符
lines = [line.strip() for line in sys.stdin.readlines()]

# 或者逐行读取（适用于不确定行数的情况），流式输入
for line in sys.stdin:
    line = line.strip()
    # 处理每一行

# 读取一行，且保留换行符（需用 .strip() 去除）
n = sys.stdin.readline().strip()
# while与读一行的方法结合实现逐行读取
while Ture:
    try:
        n = sys.stdin.readline().strip()
    except:
        break

    
# 注意 机考中默认给的是 line.split()，返回的是list
# 所以实际是 list = line.split()而非 str = line.split()


```

| 特性 | `sys.stdin.read().splitlines()` | `for line in sys.stdin:` |
|------|-------------------------------|--------------------------|
| 读取时机 | 一次性读完全部 | 惰性逐行读取 |
| 是否消耗流 | ✅ 是（后续读为空） | ✅ 是（每读一行消耗一行） |
| 返回值 | `list[str]`（可随机访问） | 迭代器（只能顺序遍历一次） |
| 内存占用 | 高（全载入内存） | 低（逐行处理） |
| 适用场景 | 输入量适中（≤10⁶ 行） | 超大输入（需流式处理） |
| 华为机试推荐 | ✅ 绝大多数情况首选 | ⚠️ 仅当明确需要流式处理 |


对比input(),它自带strip()，还有其他的额外开销，只适合小脚本，小数据，大内存。