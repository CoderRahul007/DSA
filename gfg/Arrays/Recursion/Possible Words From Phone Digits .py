class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        def helper(a,N,i,numpad,answer,result):
            if i==N:
                answer.append(result)
                return
            for j in numpad[a[i]]:
                result = result + j
                helper(a,N,i+1,numpad,answer,result)
                result = result[:len(result)-1]
            
        numpad = {1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        answer = []
        result = ""
        helper(a,N,0,numpad,answer,result)
        return answer



# Given a keypad as shown in the diagram, and an N digit number which is represented by array a[ ], 
# the task is to list all words which are possible by pressing these numbers.

# Example 1:

# Input: N = 3, a[] = {2, 3, 4}
# Output:
# adg adh adi aeg aeh aei afg afh afi 
# bdg bdh bdi beg beh bei bfg bfh bfi 
# cdg cdh cdi ceg ceh cei cfg cfh cfi 
# Explanation: When we press 2,3,4 then 
# adg, adh, adi, ... cfi are the list of 
# possible words.

