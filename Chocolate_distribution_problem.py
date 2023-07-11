'''
Given an array of N integers where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. 
There are m students, the task is to distribute chocolate packets such that: 
Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.
'''
def helper(arr,m):
    n=len(arr)
    arr.sort()
    m=arr[-1]-arr[0]
    for i in range(n-m+1):
        m=min(m,arr[m+i-1]-arr[i])
    print(m)
arr=[7, 3, 2, 4, 9, 12, 56]
m=3
helper(arr,m)


