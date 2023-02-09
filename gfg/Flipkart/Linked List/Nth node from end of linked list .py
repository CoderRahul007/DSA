def getNthFromLast(head,n):
    #code here
    temp = head
    L = 0
    while temp :
        L+=1
        temp= temp.next
    if n > L:
        return -1
    k = L-n
    temp = head
    while temp and k > 0:
        temp = temp.next
        k-=1
    return temp.data