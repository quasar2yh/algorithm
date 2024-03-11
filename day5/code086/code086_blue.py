def solution(arr, n):
    l_arr = len(arr)
    for i in range(int(l_arr%2==0),l_arr,2):
        arr[i]+=n
    return arr