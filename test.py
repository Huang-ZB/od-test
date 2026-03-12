import collections

def in_circle(p,circle,friends):
    for i in circle:
        if p in friends[i]:
            continue
        else:
            # 如果与圈内的某人不是朋友关系
            return False
    return True

def solution():
    n = int(input())
    friends = collections.defaultdict(set)
    person = set()
    for _ in range(n):
        f1,f2 = input().split(',')
        friends[f1].add(f2)
        friends[f2].add(f1)
        person.add(f1)
        person.add(f2)
    circle = []
    res = []
    def func(circle,person,res):
        if not person:
            return res.append(circle)
        for p in person:
            person.discard(p)
            # 记录的团不为空时
            if circle:
                # 若符合朋友圈关系，则加入
                if in_circle(p,circle):
                    circle.append(p)
                # 不符合则什么都不做
            else:
                circle.append(p)
            # 递归下一个元素
            func(circle,person,res)
            # 回溯
            person.add(p)
    



