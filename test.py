
# 有一个数组，每次从里面取一个以上的数，要求每次取出的组合相等，组合可以只有一个数
# 求最多的组合数

arr = list(map(int,input().split()))

def select_func(arr,start,cur_selction,res):
    cur_sum , path = cur_selction

    # 终止条件
    if start == len(arr):
        res.append(cur_selction)
        return 


    # 不选择该元素
    select_func(arr,start+1,cur_selction)

    # 选择该元素
    new_selection = [cur_sum + arr[start],path + [start]]
    select_func(arr,start+1,new_selection)
    return
    

def solution(arr):

    res = []
    select_func(arr,0,[],res)


    
