# Given a source stack, copy the contents of the source stack to destination stack maintaining 
# the same order without using extra space.
# Examples: 

# Input : Source:- |3|
#                  |2|
#                  |1|

# Output : Destination:- |3|
#                        |2|
#                        |1|

# Input : Source:- |a|
#                  |b|
#                  |c|

# Output : Destination:- |a|
#                        |b|
#                        |c|
# Approach: In order to solve this without using extra space, we first reverse the source stack,
#  then pop the top elements of the source stack one by one and push it into the destination stack.
#  We follow the below steps to reverse the source stack: 
 

# Initialize a variable count to 0.
# Pop the top element from the source stack and store it in variable topVal.
# Now pop the elements from the source stack and push them into the dest stack until the length of
#  the source stack is equal to count.
# Push topVal into the source stack and then pop all the elements in the dest stack and push them 
# into the source stack.
# Increment the value of count.
# If count is not equal to length of source stack – 1, repeat the process from step-2.

class Solution:
    def clonestack(self, st, cloned):
        # code here 
        c = 0
        while c < len(st):
            top = st.pop()
            while c != len(st):
                cloned.append(st.pop())
            st.append(top)
            while cloned:
                st.append(cloned.pop())
            c+=1
        while st:
            cloned.append(st.pop())