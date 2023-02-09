class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        if len(x)%2 != 0:
            return False
        dic = {}
        dic["("] = ")"
        dic["["] = "]"
        dic["{"] = "}"
        st = []
        for i in x:
            if i in ['{','(' ,'[']:
                st.append(i)
            else:
                if len(st) > 0:
                    t = st[-1]
                   
                    if t in dic:
                       
                        if dic[t] == i:
                            st.pop()
                        else:
                            return False
                else:
                    return False
        if len(st) > 0:
            return False
        return True