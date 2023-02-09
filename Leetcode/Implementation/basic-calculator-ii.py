#  Solution - I (Convert to Postfix & Evaluate)

# We use postfix/prefix notation because they are easier to parse and evalute.
# So, we can convert the given infix notation to postfix and then evaluate the
# postfix expression. Both are standard algorithm.

# To convert into postfix notation -

# Initialize an empty stack and iterate over the given expression string
# if character is digit, then add it to postfix string
# If character is operator, pop from stack and add to postfix string till precedence
# of stack top is greater or equal to current operator (this ensures higher precedence
# operator are evaluated first). Then push the current operator to stack
# Finally pop all remaining operators from stack and add to postfix string
# We also use separator ('|' in below code) after each number to help distinguish
#  between start and end of a number. For eg If we have 12 + 34, the postfix expression
#   is 1234+ but to help separate original numbers, we make it as 12|34|+.

# Then we evaluate postfix string as -

# Initialize an empty stack and iterate over the postfix string
# If character is digit, form the complete number and push it into stack
# If character is operator, pop top two numbers from stack, evaluate using the
# current operator and push the result back into stack.
# Finally, only one number will be present in stack which will be final result

class Solution:
    def calculate(self, s):
        def precedence(c):
            return c == '*' or c == '/'

        def toPostfix(s):
            op, post = deque(), ''
            for c in s:
                if c == ' ':
                    continue
                elif c.isdigit():
                    post += c
                else:
                    post += '|'
                    while op and precedence(c) <= precedence(op[-1]):
                        post += op.pop()
                    op.append(c)

            return post + '|' + ''.join(reversed(op))

        s, num, i = toPostfix(s), deque(), 0
        while i < len(s):
            if s[i].isdigit():
                j = s.find('|', i+1)
                num.append(int(s[i:j]))
                i = j
            else:
                num1, num2 = num.pop(), num.pop()
                if s[i] == '*':
                    num.append(num2 * num1)
                elif s[i] == '/':
                    num.append(num2 // num1)
                elif s[i] == '+':
                    num.append(num2 + num1)
                elif s[i] == '-':
                    num.append(num2 - num1)
            i += 1

        return num.pop()

########################################################################

# We can solve it without any postfix logic by observing a pattern in our evaluation.
# First thing to observe is that we are only evaluating previous seen operator and not
#  the current operator since we would need to know the next number as well before we
#   can evaluate the term using current operator.

# Now, if the previous operator was * or /, we can directly evaluate the term. Eg.
#  If we have a * b + ..., a * b / ... or a * b - ..., we can always evaluate the term
#  a * b without caring what next term would be. Same thing if it was a / b. (Note that
#  a can be individual term or intermediate result formed by cumulative result of previous
#  * & / operations...it is denoted by interimRes in below code)

# However, if the previous operator was + or -, the evaluation depends on current operator.
#  For eg. In a + b - ..., we can evaluate a + b and we would get correct result in both
#   cases. But in a + b * ..., evaluating a + b would give wrong result. Same thing if it was a - b.
# So, if current operator is * or /, then we need to add a to the final result and later
#  add result of remaining expression later. If current operator is + or -,
#  we can either do the same thing by adding a to final result or evaluate a + b
#  term & add to result. But to decouple the case from current operator and to generalize
#  the case, in both cases, we will only add a to the final result & later add result of remaining expression.

# So, we have following cases -

# previous operator was * or /:
# Directly evaluate 1st term - a * b or a / b. This is denoted as interimRes *= cur or
#  interimRes /= cur in below code)
# Maintain interimRes as we may need it if future operators are * or / as well.
# previous operator was + or -:
# Add a to final result and later we will add the result of remaining expression.
#  Thus, in below code, we first add interimRes to final ans.
# Then, update interimRes to hold remaining expression found till now, i.e, ±cur
#  depending on prevOp.


class Solution:
    def calculate(self, s):
        cur, ans, interimRes, prevOp = 0, 0, 0, '+'
        for c in s + '##':
            if c == ' ':
                continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if prevOp == '*':
                    interimRes *= cur
                elif prevOp == '/':
                    interimRes = trunc(interimRes / cur)
                else:
                    ans += interimRes
                    interimRes = cur if prevOp == '+' else -cur
                prevOp, cur = c, 0
        return ans
