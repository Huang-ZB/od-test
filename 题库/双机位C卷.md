
## 天然蓄水池
公元2919年，人类终于发现了一颗宜居星球——X星。
现想在X星一片连绵起伏的山脉间建一个天热蓄水库，如何选取水库边界，使蓄水量最大？

要求：

        山脉用正整数数组s表示，每个元素代表山脉的高度。
        选取山脉上两个点作为蓄水库的边界，则边界内的区域可以蓄水，蓄水量需排除山脉占用的空间
        蓄水量的高度为两边界的最小值。
        如果出现多个满足条件的边界，应选取距离最近的一组边界。
输出边界下标（从0开始）和最大蓄水量；如果无法蓄水，则返回0，此时不返回边界。
例如，当山脉为s=[3,1,2]时，则选取s[0]和s[2]作为水库边界，则蓄水量为1，此时输出：0 2:1
当山脉s=[3,2,1]时，不存在合理的边界，此时输出：0。

给定一个长度为 n 的整数数组 height 。数组的元素表示山的高度，选择两个元素作为水库的边界，求蓄水量的最大值并输出蓄水量最大时的边界下标（蓄水量相同时输出下标较近的）。

输入描述：

输入一行数字，空格分隔。

输出描述：

输出蓄水量的最大值及输出蓄水量最大时的边界下标

示例1：

输入：

1 8 6 2 5 4 8 3 7 

输出：

1 6:15

说明：蓄水量的最大值为 15

蓄水量最大时的边界下标为1 和 6

### 答案

```python
high = [int(i) for i in input().split()]

n = len(high)
hi = n-1
lo = 0

S_max = 0
index = [lo,hi]
while lo < hi -1:
    min_bian = min(high[lo],high[hi])
    S = min_bian*(hi-lo-1)
    # 剪枝
    if S < S_max:
        if high[lo] > high[hi]:
            hi -= 1
        else:
            lo += 1
        continue

        
    for i in range(lo+1,hi):
        if high[i] >= min_bian:
            S -= min_bian
        else:
            S -= high[i]
    if S >= S_max:
        S_max = S
        index = [lo,hi]
    
    if high[lo] > high[hi]:
        hi -= 1
    else:
        lo += 1


if S_max == 0:
    print(0)
else:
    print(" ".join(map(str,index)),end=":")
    print(S_max)
```


## 采购订单
在一个采购系统中，采购申请(PR)需要经过审批后才能生成采购订单(PO)。每个PR包含商品的单价(假设相同商品的单价一定是一样的)及数量信息。系统要求对商品进行分类处理:单价高于100元的商品需要单独处理，单价低于或等于100元的相同商品可以合并到同一采购订单PO中。针对单价低于100的小额订单，如果量大可以打折购买。
具体规则如下:
如果PR状态为"审批通过"，则将其商品加入到PO中。如果PR的状态为"审批拒绝"或"待审批"，则忽略改PR,对于单价高于100元的商品、每个商品单独生成一条PO记录。对于单价低于100元的商品，将相同商品的数量合并四到一条PO记录中。如果商品单价<100且商品数量>=100，则单价打9折。
输入描述
第一行包含整数N，表示PR的数量。
接下来N行，每行包含四个用空格分割的整数，按顺序表示:商品ID,数量，单价，PR状态(0表示审批通过，1表示审批拒绝，2表示待审批)
输出描述
输出若干行，每行表示一条PO记录，按以下格式输出:
对于单价高于100元的商品:商品ID 数量 单价
对于单价低于或等于100元的商品:商品ID 总数量 打折后的单价(向上取整)输出的PO记录按商品ID升序升序排列，相同商品按照数量降序排列
补充
2<=n<= 1000
1<= 商品价格 <= 200
1 <= 商品数量 <= 1000
2<= 商品编号 <= 1000

示例1：

输入

2
1 200 90 0
2 30 101 0
 

输出

1 200 81
2 30 101
 

说明：

商品1的原始单价为90，审批通过，生成一条PO，满足打折条件，打折后单价为81。商品2的单价为101，审批通过，生成一条PO

示例2：

输入

3
1 10 90 0
1 5 90 0
2 8 120 0
 

输出

1 15 90
2 8 120
 

说明：

PR1和PR2均为商品1，单价90，审批通过，单价低于100元，合并数量为150.PR3为商品2，单价120元，审批通过，单价高于100元，单独生成一条PO记录

示例3：

输入

4
1 5 80 0
2 3 120 0
3 2 90 1
4 10 150 2
 

输出

1 5 80
2 3 120
 

说明：

PR1:商品1，单价80元，审批通过，单价低于100元，合并到PO中。

PR2:商品2，单价120元，审批通过，单价高于100元，单独生成一条PO记录。PR3:审批拒绝，忽略。PR4待审批忽略。

## P00308. 出差 / 员工派遣
某公司部门需要派遣员工去国外做项目。
现在，代号为 x 的国家和代号为 y 的国家分别需要 cntx 名和 cnty 名员工部门每个员工有一个员工号 (1,2,3,......)，工号连续，从 1开始。部长派遣员工的规则:
规则1: 从 1,k中选择员工派遣出去
规则2: 编号为 x的倍数的员工不能去 x国，编号为 y 的倍数的员工不能去y 国
问题
找到最小的k，使得可以将编号在 [1,k] 中的员工分配给 x 国和 y 国，且满足 x 国和 y 国的需求

输入描述
四个整数 x,y,cntx,cnty。
2 < x < y < 30000
x和y 一定是质数
1 < cntx, cnty < 10^9
 cntx + cnty < 10^9
输出描述
满足条件的最小的 k

示例1：

输入：

2 3 3 1

输出：

5

说明:

输入中：
2 表示国家代号 2
3 表示国家代号 3
3 表示国家 2 需要3 个人

1 表示国家 3 需要1个人

输出的5表示k最小为5


### 思路
存在三种情况：
只能去其中一个国家；
两个国家都不能去；
两个国家都可以去

由于是质数，可以直接计算而不用一个一个遍历
x//k,y//k; y//(x*y) ; k - (前面的总和) （容斥原理）

优化：
由于是x，y<30000; 可以设置一个k=1000，000，000；再用二分法去做
或者
k=2 每次扩大一倍的方式，找到某个Kmax；在 [Kmax/2,Kmax]区间通过二分法查找

```python
x,y,cntx,cnty = map(int,input().split())

k = 1
cur_z =0
# 通用型人员 = 剩余的需求数量时退出循环
while cur_z < cntx + cnty:
    flag_x = 0
    flag_y = 0
    if k % x:
        flag_x = 1
    if k % y:
        flag_y = 1
    # 如果两个国家都可以去cur_z+1
    if flag_x and flag_y:
        cur_z += 1
    else:
        # 只能分配给某个国家，则对应的需求数-1
        # 同时需求书必须大于0
        if flag_x == 1 and cntx>0:
            cntx -= 1
        if flag_y == 1 and cnty >0:
            cnty -= 1
            
    k += 1

print(k-1)
```
## P00007. 华为od机试—小明减肥
小明有n个可选运动，每个运动有对应卡路里，想选出其中k个运动且卡路里和为t。k，t，n都是给定的。求出可行解数量
输入描述
第一行输入n t k
第二行输入 每个运动的卡路里 按照空格进行分割
备注
0<n<10
t>0，0<k<=n
每个运动量的卡路里>0
输出描述
求出可行解数量

示例1：

输入

4 3 2
1 1 2 3

输出

2

说明
可行解为2，选取{0,2},{1,2}两种方式。
### 思路
经典的组合选择问题,在n个元素中选择k个元素.
遍历方法:
对于每个元素有两种情况,选和不选;每个选择背后都要递归一次
结构:
模型时一个n深度的二叉树
优化:
对于选择超过k个元素和k个元素不符合某种条件时(根据题意),剪枝
终止条件别忘了:深度小于等于n

```python
import sys

# with open("test.txt", "r", encoding="utf-8") as f:
#     sys.stdin = f
n, t, k = [int(i) for i in input().split()]
krl = [int(i) for i in input().split()]

# 求k个和为t的组合


# 对于每个数有选和不选的策略
def solution(n, t, k, krl, index, pre_sum, pre_quantity, result, ans):
    # 对于当前的数
    if index > n - 1:
        return
    # 不选择
    solution(n, t, k, krl, index + 1, pre_sum, pre_quantity, result, ans)

    # 选择
    cur_sum = pre_sum + krl[index]
    cur_quantity = pre_quantity + 1
    if cur_sum > t:
        return
    if cur_quantity > k:
        return
    if cur_quantity == k and cur_sum == t:
        ans.append(result + [index])
        return
    else:
        solution(n, t, k, krl, index + 1, cur_sum, cur_quantity, result + [index], ans)
    return


ans = []
result = []
pre_sum = 0
pre_quantity = 0
solution(n, t, k, krl, 0, 0, 0, result, ans)
print(len(ans))

```
## P00206. 华为od机试—螺旋数组矩阵/数字螺旋矩阵
疫情期间，小明隔离在家，百无聊赖，在纸上写数字玩。他发明了一种写法:
给出数字个数n和行数m(1 < n,m < 999)，从左上角的1开始，按照顺时针螺旋向内写方式，依次写出2,3...n,最终形成个一m行矩阵。
小明对这个矩阵有些要求
1.每行数字的个数一样多
2.列的数量尽可能少
3.填充数字时优先填充外部
4.数字不够时，使用单个*号占位
输入描述
输入一行，两个整数，空格隔开，依次表示n、m
输出描述
符合要求的唯一矩阵


示例1：
输入

9 4
输出
1 2 3

* * 4

9 * 5

8 7 6

示例2：
输入
3 5
输出
1

2

3

*

*


### 思路
优化：利用方向引索取模来实现更好的转向
方向数组按顺时针排列，实现顺时针90度转弯
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d_idx = 0  # 当前方向索引
d_idx = (d_idx + 1) % 4 # 顺时针旋转90度


```python
import sys
import sys

# 读取输入
try:
    line = sys.stdin.read().split()
    if not line:
        exit()
    n = int(line[0])
    m = int(line[1])
except ValueError:
    exit()

# 1. 计算列数 col
# 题目要求：每行数字个数一样多，列的数量尽可能少
# 即 col = ceil(n / m)
if n % m == 0:
    col = n // m
else:
    col = n // m + 1

# 2. 初始化矩阵，全部填 '*'
matrix = [["*"] * col for _ in range(m)]

# 3. 定义方向和初始状态
# 方向顺序：右(0,1) -> 下(1,0) -> 左(0,-1) -> 上(-1,0)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d_idx = 0  # 当前方向索引

x, y = 0, 0  # 当前位置
matrix[x][y] = 1  # 填入第一个数

# 4. 开始螺旋填充 2 到 n
for num in range(2, n + 1):
    # 计算下一个理论位置
    dx, dy = dirs[d_idx]
    nx, ny = x + dx, y + dy
    
    # 判断是否需要转向：
    # 条件1: 越界 (nx < 0 or nx >= m or ny < 0 or ny >= col)
    # 条件2: 该位置已经被填充 (matrix[nx][ny] != '*')
    if nx < 0 or nx >= m or ny < 0 or ny >= col or matrix[nx][ny] != "*":
        # 改变方向 (顺时针转90度)
        d_idx = (d_idx + 1) % 4
        dx, dy = dirs[d_idx]
        nx, ny = x + dx, y + dy
    
    # 更新位置并填入数字
    x, y = nx, ny
    matrix[x][y] = num

# 5. 输出结果
for row in matrix:
    print(" ".join(map(str, row)))

```

## P00152. 华为od机试—查找接口成功率最优时间段

服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，

数组中每个元素都是单位时间内失败率数值，数组中的数值为0~100的整数，

给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于minAverageLost，

找出数组中最长时间段，如果未找到则直接返回NULL。

输入描述

输入有两行内容，第一行为{minAverageLost}，第二行为{数组}，数组元素通过空格(” “)分隔，

minAverageLost及数组中元素取值范围为0~100的整数，数组元素的个数不会超过100个。

输出描述

找出平均值小于等于minAverageLost的最长时间段，输出数组下标对，格式{beginIndex}-{endIndx}(下标从0开始)，

如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格(” “)拼接，多个下标对按下标从小到大排序。

示例1 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

1

0 1 2 3 4

输出

0-2

说明

输入解释：minAverageLost=1，数组[0, 1, 2, 3, 4]

前3个元素的平均值为1，因此数组第一个至第三个数组下标，即0-2


## #P00152. 华为od机试—查找接口成功率最优时间段
服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，

数组中每个元素都是单位时间内失败率数值，数组中的数值为0~100的整数，

给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于minAverageLost，

找出数组中最长时间段，如果未找到则直接返回NULL。

输入描述

输入有两行内容，第一行为{minAverageLost}，第二行为{数组}，数组元素通过空格(” “)分隔，

minAverageLost及数组中元素取值范围为0~100的整数，数组元素的个数不会超过100个。

输出描述

找出平均值小于等于minAverageLost的最长时间段，输出数组下标对，格式{beginIndex}-{endIndx}(下标从0开始)，

如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格(” “)拼接，多个下标对按下标从小到大排序。

示例1 输入输出示例仅供调试，后台判题数据一般不包含示例

输入

1
0 1 2 3 4

输出

0-2

说明

输入解释：minAverageLost=1，数组[0, 1, 2, 3, 4]

前3个元素的平均值为1，因此数组第一个至第三个数组下标，即0-2

### 思路
直接暴力两层遍历
注意读题，没有要返回NULL

```python
import sys

# with open("test.txt", "r", encoding="utf-8") as f:
#     sys.stdin = f
#     n, t, k = [int(i) for i in input().split()]
#     krl = [int(i) for i in input().split()]

min_ave = int(input())
arr = list(map(int,input().split()))

S = [0] * (len(arr)+1)
for i in range(1,len(S)):
    S[i] = S[i-1] + arr[i-1]

max_len = 0
ans = []
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        cur_sum = S[j+1] - S[i]
        cur_len = j-i+1
        cur_ave = cur_sum/(cur_len)
        if cur_ave > min_ave:
            continue
        if max_len < cur_len:
            max_len = cur_len
            ans = [f'{i}-{j}']
        elif max_len == cur_len:
            ans.append(f'{i}-{j}')

if ans:
    print(" ".join(ans))
else:
    print("NULL")
```
## P00237. 华为od机试—竖直四子棋
![alt text](image.png)
![alt text](image-1.png)
竖直四子棋的棋盘是竖立起来的，双方轮流选择棋盘的一列下子，棋子因重力落到棋盘底部或者其他棋子之上，当一列的棋子放满时，无法再在这列上下子。
一方的4个棋子横、竖或者斜方向连成一线时获胜。
现给定一个棋盘和红蓝对弈双方的下子步骤，判断红方或蓝方是否在某一步获胜。
下面以一个6×5的棋盘图示说明落子过程：



下面给出横、竖和斜方向四子连线的图示：



输入描述
输入为2行，第一行指定棋盘的宽和高，为空格分隔的两个数字；
第二行依次间隔指定红蓝双方的落子步骤，第1步为红方的落子，第2步为蓝方的落子，第3步为红方的落子，以此类推。
步骤由空格分隔的一组数字表示，每个数字为落子的列的编号（最左边的列编号为1，往右递增）。用例保证数字均为32位有符号数。
输出描述
如果落子过程中红方获胜，输出 N,red ；
如果落子过程中蓝方获胜，输出 N,blue ；
如果出现非法的落子步骤，输出 N,error。
N为落子步骤的序号，从1开始。如果双方都没有获胜，输出 0,draw 。
非法落子步骤有两种，一是列的编号超过棋盘范围，二是在一个已经落满子的列上落子。
N和单词red、blue、draw、error之间是英文逗号连接。
示例1 输入输出示例仅供调试，后台判题数据一般不包含示例
输入
5 5
1 1 2 2 3 3 4 4
输出
7,red
说明
在第7步，红方在第4列落下一子后，红方的四个子在第一行连成一线，故红方获胜，输出 7,red。
示例2 输入输出示例仅供调试，后台判题数据一般不包含示例
输入
5 5
0 1 2 2 3 3 4 4
输出
1,error
说明
第1步的列序号为0，超出有效列编号的范围，故输出 1,error。

### 思路和易错点
1 注意检查时要正负方向都要检查
2 找到落子点后记得break

```python

width,height = list(map(int, input().split()))
arr = list(map(int, input().split()))

def check(matrix,row,col,width,height):
    # 检查四个方向，横，纵，对角，斜对角
    # 注意是以自己为中心在该方向上左右检查
    forward = {(0,1),(1,0),(1,1),(1,-1)}
    for way in forward:
        dx,dy = way
        # 只需要找三个
        cnt = 0
        # 正方向
        new_row = row + dx
        new_col = col + dy
        while 0 <= new_col < width and 0<= new_row < height:
            if matrix[new_row][new_col] == matrix[row][col]:
                cnt +=1
            else:
                break
            if cnt == 3 :
                return True
            new_row += dx
            new_col += dy
        # 负方向
        new_row = row-dx
        new_col = col-dy
        while 0 <= new_row < width and 0<= new_col < height:
            if matrix[new_row][new_col] == matrix[row][col]:
                cnt +=1
            else:
                break
            if cnt == 3 :
                return True
            new_row -= dx
            new_col -= dy
    return False

def solution(arr,width,height):
    color = {1:"red",2:"blue"}
    len_arr = len(arr)
    matrix =  [ [0]*width for i in range(height) ]
    for i in range(len_arr):
        # 从第0步开始，初始为红色1，即偶数为1
        turn = 1 if i % 2 == 0 else 2
        bushu = i+1
        # 落子
        # 列从0开始，要减1
        col = arr[i] - 1
        # 检查列是否合法
        if col < 0 or col >= width:
            return f"{bushu},error"

        # # 查找落子位置
        # row_idx = -1
        # for j in range(height-1,-1,-1):
        #     if matrix[j][col] == 0:
        #         row_idx = j
        #         break
        # # 如果未找到，说明列满了
        # if row_idx == -1:
        #     return f"{bushu},error"
        # else:
        #     matrix[row_idx][col] = turn

        # if check(matrix,row_idx,col,width,height):
        #     return f"{bushu},{color[turn]}"

        # 检查列是否落满
        if matrix[0][col] != 0:
            return f"{bushu},error"
        # 棋盘落子会落到最下面，所以从最后一行开始
        for row in range(height-1,-1,-1):
            if matrix[row][col] ==0:
                matrix[row][col] = turn
                res = check(matrix,row,col,width,height)
                if res:
                    return f"{bushu},{color[turn]}"
                # 不要忘记break
                break
    # 下完所有步数都没有返回值说明和局
    return "0,draw"
            
print(solution(arr,width,height))
```

## P00408. 华为od机试—网格红绿灯最短路径【2025新题】
给定一个二维的m*n网格地图(grids二维数组)，每个单元格0为空，1是障碍物，2是红绿灯;每一步可以在0或者2的单元格移动，每一秒可以走一个单元格;遇到红绿灯想要通过需要等待不同的时间才能通过，大小为x的light数组标注灯的坐标和等待时间，例如(2,2.3),坐标(2,2)红绿灯等待时间3秒，问从左上角(0,0)到右下角(m-1,n-1)所需的最短时间。

输入描述
第一行输入 grids 二维数组，内部数据只有0，1，2，1<m,n<=100
第二行输入 lights 红绿灯二维数组，1<x<=m*n
输出描述
从坐标(0,0)到(m-1,n-1)坐标所需的最短时间，如果没有路径，则返回最短时间为-1.

示例1
输入
[[0,1,0],[0,2,1],[0,0,0]]
[[1,1,3]]
输出
4


```python
import ast
import heapq
grids = ast.literal_eval(input())
lights = ast.literal_eval(input())
# grids = ast.literal_eval('[[0,1,0],[0,2,1],[0,0,0]]')
# lights = ast.literal_eval('[[1,1,3]]')

lights_dict = {}
for light in lights:
    row,col,time = light
    lights_dict[(row,col)] = time




def dijkstra(grids,lights_dict,min_grids,start,target,pretime,rown,coln):
    ways = {(0,1),(0,-1),(1,0),(-1,0)}
    # 处理源点
    x,y = start
    pq = [(pretime,x,y)]
    
    while pq:
        # 弹出 源点到目标点耗时最短
        cur_time,cur_x,cur_y = heapq.heappop(pq)
        # 与记录的最短时间表进行比较，若时间更长说明不是最短，直接剔除
        if cur_time > min_grids[cur_x][cur_y]:
            continue
        
        # 查找邻接点
        for way in ways:
            dx,dy = way
            newx = cur_x + dx
            newy = cur_y + dy
            # 检查是否越界
            if  newx < 0 or newx >= rown or newy < 0 or newy >= coln:
                continue
            # 查看是否能通过
            if grids[newx][newy] == 1:
                continue
            
            # 经过时间
            througth_time = 1
            # 等待时间
            wait_time = 0
            if grids[newx][newy] == 2:
                wait_time = lights_dict[(newx,newy)]
            # 源点到该点的时间
            tatol_time = cur_time + througth_time + wait_time

            if tatol_time < min_grids[newx][newy]:
                min_grids[newx][newy] = tatol_time
                heapq.heappush(pq,(tatol_time,newx,newy))
    return


def solution(grids,lights_dict):
    # 检查地图是否为空
    if not grids:
        return -1
    # 检查起始点，终点是否为障碍物
    rown = len(grids)
    coln = len(grids[0])
    start = (0,0)
    target = (rown-1,coln-1)
    if grids[0][0] == 1 or grids[rown-1][coln-1] == 1:
        return -1
    min_grids = [[float("inf")]*coln for _ in range(rown)]
    # 起始点的等待时间
    pretime = 0
    if grids[0][0] == 2:
        pretime += lights_dict.get(start,0)
    min_grids[0][0] = pretime

    dijkstra(grids,lights_dict,min_grids,start,target,pretime,rown,coln)
    
    if min_grids[rown-1][coln-1] == float('inf'):
        return -1
    else:
        return min_grids[rown-1][coln-1]
    

print(solution(grids,lights_dict))

```
## P00115. 华为od机试—打印机队列 / 打印文件

有5台打印机打印文件，每台打印机有自己的待打印队列。因为打印的文件内容有轻重缓急之分，

所以队列中的文件有1~10不同的代先级，其中数字越大优先级越高。

打印机会从自己的待打印队列中选择优先级最高的文件来打印。

如果存在两个优先级一样的文件，则选择最早进入队列的那个文件。

现在请你来模拟这5台打印机的打印过程。

输入描述

每个输入包含1个测试用例，每个测试用例第一行给出发生事件的数量N（0 < N < 1000）。
接下来有 N 行，分别表示发生的事件。
共有如下两种事件：
1. “IN P NUM”，表示有一个拥有优先级 NUM 的文件放到了打印机 P 的待打印队列中。（0< P <= 5, 0 < NUM <= 10)；
2. “OUT P”，表示打印机 P 进行了一次文件打印，同时该文件从待打印队列中取出。（0 < P <= 5）。

输出描述

对于每个测试用例，每次”OUT P”事件，请在一行中输出文件的编号。
如果此时没有文件可以打印，请输出”NULL“。
文件的编号定义为”IN P NUM”事件发生第 x 次，此处待打印文件的编号为x。编号从1开始。

示例1   输入输出示例仅供调试，后台判断数据一般不包含示例

输入

7
IN 1 1
IN 1 2
IN 1 3
IN 2 1
OUT 1
OUT 2
OUT 2

输出

3
4
NULL

### 优化
使用堆排序
```python
from bisect import bisect_left

N = int(input())
file_num = 1
dict_p = {}
for i in range(N):
    arr = list(input().split(" "))
    # 如果时输入事件
    if arr[0] == "IN":
        P,NUM = int(arr[1]) , int(arr[2])
        # 升序排序，相同优先级文件号大的会排在后面，所以取负
        item = (NUM,-file_num)
        if P in dict_p:
            q = dict_p[P]
            idx = bisect_left(q,item)
            q.insert(idx,item)
            
        else:
            dict_p[P] = [item]
        file_num += 1

    
    if arr[0] == "OUT":
        P = int(arr[1])
        if P in dict_p and len(dict_p[P]) > 0:
            print(-dict_p[P].pop()[1])
        else:
            print("NULL")
```

## P00410. 华为od机试—优雅子数组
如果一个数组中出现次数最多的元素出现大于等于K次，被称为K -优雅数组，k也可以被称为优雅阈值。例如，数组1，2，3，1、2，3，1，它是一个3-优雅数组，因为元素1出现次数大于等于3次，数组1,2,3,1,2就不是一个3-优雅数组，因为其中出现次数最多的元素是1和2，只出现了2次。
给定一个数组A和k，请求出A有多少子数组是k-优雅子数组。
子数组是数组中一个或多个连续元素组成的数组。
例如，数组[1.2.3.4]包含10个子数组，分别是:
[1], [1,2], [1,2,3], [1,2,3,], [2], [2,3], [2,3,4], [3], [3,4] , [4]
输入描述
第一行输入两个数字，以空格隔开，含义是: A数组长度 k值
第二行输入A数组元素，以空格隔开
输出描述
输出A有多少子数组是k-优雅子数组

示例1：

输入：

7 3
1 2 3 1 2 3 1

输出：

1
### 优化
下面的方法比较暴力
利用双指针和可变的滑动窗口
当窗口内的某个元素出现次数==k是，直接剪枝，含有[left,right]的数组都成立，即n-right +1个
此时开始左指针，并减去相应的次数直至找到与arr[right]相同的元素，使其=k-1
之后在移动右指针，重复上述操作

```python 

n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
def solution(arr,n,k):
    ans = 0
    if n < k:
        return 0
    # 遍历某位置为起始的所有数组
    for i in range(n-k+1):
        
        dict_sub = {}
        for j in  range(i,n):
            # dictsub记录i——j区间的子数组的出现次数，若出现某元素=k，其后面的更长的子数组也符合条件
            if arr[j] not in dict_sub:
                dict_sub[arr[j]] = 0
            dict_sub[arr[j]] += 1
            if dict_sub[arr[j]] == k:
                ans += n - j
                break
    return ans
        

print(solution(arr,n,k))

```

## P00402. 华为od机试—叠积木

有一堆长方体积木，它们的长度和宽度都相同，但长度不一。

小橙想把这堆积木叠成一面墙，墙的每层可以放一个积木，也可以将两个积木拼接起来，要求每层的长度相同。

若必须用完这些积木，叠成的墙最多为多少层？

如下是叠成的一面墙的图示，积木仅按宽和高所在的面进行拼接。



输入描述：

输入为一行，为各个积木的长度，数字为正整数，并由空格分隔。积木的数量和长度都不超过5000。

输出描述：

输出一个数字，为墙的最大层数，如果无法按要求叠成每层长度一致的墙，则输出-1。

输入

给定积木的长度，以空格分隔，例如:3 6 6 3。

输出

如果可以搭建，返回最大层数，如果不可以返回-1。

示例1   输入输出示例仅供调试，后台判题数据一般不包含示例

输入

3 6 6 3

输出

3

解释：以 6 为底的墙，第一层为 6 ，第二层为 6，第三层 3 + 3。

示例2   输入输出示例仅供调试，后台判题数据一般不包含示例

输入

1 4 2 3 6

输出

-1

解释：

无法组成长度相同的结果
