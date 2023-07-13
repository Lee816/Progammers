def solution(arr1, arr2):
    if len(arr1)>len(arr2) or len(arr1)==len(arr2) and sum(arr1)>sum(arr2):
        return 1
    if len(arr1)<len(arr2) or len(arr1)==len(arr2) and sum(arr1)<sum(arr2):
        return -1
    if len(arr1)==len(arr2) and sum(arr1)==sum(arr2):
        return 0