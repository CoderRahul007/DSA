# arrr - [ 2 , 3 , 1]
# ans - [ -1 , 2 , 2] i.e prev smaller element of the current element

# Using Stack
def nextSmallerElement( arr ):
    st = [-1]
    ans = [0]*len(arr)
    n = len(arr)
    for i in range(n):
        ele = arr[i]
        if st and st[-1] > ele:
            st.pop()
        ans[i] = st[-1]
        st.append(ele)
    print(ans)