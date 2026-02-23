# =====================================================
# 导入必要的模块
# =====================================================
import sys
from typing import List, Tuple

# 设置递归深度限制，防止线段树递归过深导致栈溢出
sys.setrecursionlimit(300000)

# =====================================================
# 线段树节点类
# =====================================================
class Node:
    """
    线段树节点，存储区间内的统计信息

    需要维护6个值：
    - rcnt: 'r' 字符的个数
    - ecnt: 'e' 字符的个数
    - dcnt: 'd' 字符的个数
    - recnt: "re" 子序列的个数
    - edcnt: "ed" 子序列的个数
    - redcnt: "red" 子序列的个数（最终答案）
    """
    def __init__(self):
        self.rcnt = 0    # 区间内字符 'r' 的个数
        self.ecnt = 0    # 区间内字符 'e' 的个数
        self.dcnt = 0    # 区间内字符 'd' 的个数
        self.recnt = 0   # 区间内 "re" 子序列的个数
        self.edcnt = 0   # 区间内 "ed" 子序列的个数
        self.redcnt = 0  # 区间内 "red" 子序列的个数

    def __repr__(self):
        """方便调试打印"""
        return f"Node(r={self.rcnt}, e={self.ecnt}, d={self.dcnt}, re={self.recnt}, ed={self.edcnt}, red={self.redcnt})"


# =====================================================
# 线段树类
# =====================================================
class SegmentTree:
    """
    线段树实现，支持单点修改和区间查询

    核心思想：
    1. 每个节点维护区间内的字符统计信息
    2. 合并两个区间时，需要考虑跨区间的子序列组合
    3. 单点修改后，从叶子节点向上更新所有祖先节点
    """

    def __init__(self, s: str):
        """
        初始化线段树

        参数:
            s: 字符串（1-indexed，前面有空格）
        """
        self.n = len(s) - 1  # 字符串实际长度（减1是因为前面有空格）
        self.s = s  # 保存原始字符串，方便更新
        self.tree: List[Node] = [Node() for _ in range(4 * self.n + 5)]
        # 线段树数组大小：4*n足够存储所有节点

        # 在对象创建完成后，立即构建线段树
        self._build(1, self.n, 1)

    def _ls(self, p: int) -> int:
        """获取左子节点索引"""
        return p << 1  # 等价于 p * 2

    def _rs(self, p: int) -> int:
        """获取右子节点索引"""
        return (p << 1) | 1  # 等价于 p * 2 + 1

    def _push_up(self, p: int):
        """
        合并左右子节点信息，更新当前节点

        这是线段树的核心操作！

        合并原理：
        1. 单个字符数量：左右区间直接相加
        2. 两字符子序列：左区间 + 右区间 + 跨区间组合
        3. 三字符子序列：四种情况相加
        """
        left = self.tree[self._ls(p)]   # 左子节点
        right = self.tree[self._rs(p)]  # 右子节点
        curr = self.tree[p]             # 当前节点

        # ========== 单个字符数量：直接相加 ==========
        curr.rcnt = left.rcnt + right.rcnt
        curr.ecnt = left.ecnt + right.ecnt
        curr.dcnt = left.dcnt + right.dcnt

        # ========== "re"子序列数量 ==========
        # 三种情况：
        # 1. 完全在左区间：left.recnt
        # 2. 完全在右区间：right.recnt
        # 3. 跨区间：左区间的每个'r' + 右区间的每个'e'
        #    为什么是乘法？因为左区间有left.rcnt个'r'，
        #    右区间有right.ecnt个'e'，每个'r'都能和每个'e'组合
        curr.recnt = left.recnt + right.recnt + left.rcnt * right.ecnt

        # ========== "ed"子序列数量 ==========
        # 同理：左区间的每个'e' + 右区间的每个'd'
        curr.edcnt = left.edcnt + right.edcnt + left.ecnt * right.dcnt

        # ========== "red"子序列数量 ==========
        # 四种情况：
        # 1. 完全在左区间：left.redcnt
        # 2. 完全在右区间：right.redcnt
        # 3. "re"在左区间，"d"在右区间：left.recnt * right.dcnt
        #    左区间有left.recnt个"re"，右区间有right.dcnt个'd'
        #    每个"re"都能和每个'd'组成"red"
        # 4. "r"在左区间，"ed"在右区间：left.rcnt * right.edcnt
        #    左区间有left.rcnt个'r'，右区间有right.edcnt个"ed"
        #    每个'r'都能和每个"ed"组成"red"
        curr.redcnt = (left.redcnt + right.redcnt +
                      left.recnt * right.dcnt +
                      left.rcnt * right.edcnt)

    def _build(self, l: int, r: int, p: int):
        """
        构建线段树（递归）

        参数:
            l: 当前区间左端点
            r: 当前区间右端点
            p: 当前节点索引
        """
        if l == r:
            # 叶子节点：只包含一个字符
            char = self.s[l]
            if char == 'r':
                self.tree[p].rcnt = 1
            elif char == 'e':
                self.tree[p].ecnt = 1
            elif char == 'd':
                self.tree[p].dcnt = 1
            # 其他字符所有计数都是0，不需要处理
            return

        # 非叶子节点：递归构建左右子树
        mid = (l + r) // 2  # 计算中点
        self._build(l, mid, self._ls(p))      # 构建左子树
        self._build(mid + 1, r, self._rs(p))  # 构建右子树

        # 合并左右子树信息
        self._push_up(p)

    def _update(self, pos: int, char: str, l: int, r: int, p: int):
        """
        单点修改（递归）

        参数:
            pos: 要修改的位置
            char: 新字符
            l: 当前区间左端点
            r: 当前区间右端点
            p: 当前节点索引
        """
        if l == r and l == pos:
            # 找到目标位置，重置节点
            self.tree[p] = Node()

            # 根据新字符设置计数
            if char == 'r':
                self.tree[p].rcnt = 1
            elif char == 'e':
                self.tree[p].ecnt = 1
            elif char == 'd':
                self.tree[p].dcnt = 1
            return

        # 递归查找目标位置
        mid = (l + r) // 2
        if pos <= mid:
            # 目标位置在左子树
            self._update(pos, char, l, mid, self._ls(p))
        else:
            # 目标位置在右子树
            self._update(pos, char, mid + 1, r, self._rs(p))

        # 更新后需要重新合并左右子树信息
        self._push_up(p)

    def modify(self, pos: int, char: str):
        """
        对外提供的修改接口

        参数:
            pos: 要修改的位置（1-indexed）.1-indexed表示为从1开始的计数凡方式
            char: 新字符
        """
        self._update(pos, char, 1, self.n, 1)
        self.s = self.s[:pos] + char + self.s[pos+1:]  # 更新原字符串

    def get_red_count(self) -> int:
        """
        获取"red"子序列总数

        返回:
            整个字符串中"red"子序列的数量
        """
        return self.tree[1].redcnt  # 根节点存储整个区间的信息


# =====================================================
# 主函数
# =====================================================
def main():
    """
    主函数：处理输入输出和查询
    """
    # 优化输入输出速度（Python中很重要！）
    input = sys.stdin.readline

    # 读入字符串长度和操作次数
    n, q = map(int, input().split())

    # 读入两个字符串
    s = input().strip()
    t = input().strip()

    # 在字符串前添加空格，使其变为1-indexed
    # 这样处理更方便，下标从1开始，与题目描述一致
    s = " " + s
    t = " " + t

    # 为两个字符串分别建立线段树
    tree_s = SegmentTree(s)
    tree_t = SegmentTree(t)

    # 处理每次操作
    results = []  # 存储所有结果，最后一起输出（比逐行输出快）

    for _ in range(q):
        x = int(input())  # 读入要交换的位置

        # 交换 s[x] 和 t[x]
        # Python字符串不可变，需要转换为列表或使用切片
        temp = s[x]
        s = s[:x] + t[x] + s[x+1:]
        t = t[:x] + temp + t[x+1:]

        # 在线段树中更新这两个位置
        tree_s.modify(x, s[x])
        tree_t.modify(x, t[x])

        # 计算并存储两个字符串"red"子序列数量的差值
        diff = tree_s.get_red_count() - tree_t.get_red_count()
        results.append(str(diff))

    # 一次性输出所有结果（比逐行输出快）
    print('\n'.join(results))


# =====================================================
# 程序入口
# =====================================================
if __name__ == "__main__":
    main()
