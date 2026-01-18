# sys 模块
## 标题2
1 sys.stdin 标准输入

```python
import sys
<u>一次性</u>
# 一次性读取所有输入并按行分割
lines = sys.stdin.read().splitlines()

# 或者逐行读取（适用于不确定行数的情况）
for line in sys.stdin:
    line = line.strip()
    # 处理每一行

# 读取一行，且保留换行符（需用 .strip() 去除）
n = sys.stdin.readline().strip() 
```

