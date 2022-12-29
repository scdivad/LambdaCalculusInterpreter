from sympy import *

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
LAMBDA = 'λ'

def eval_expr(expression):
    print("sent to eval: " + expression)
    expression = expression.replace('^', '**')
    ret = str(simplify(expression))
    ret = ret.replace('**', '^')
    return ret

def parse(s, simpl=False):
    # case where s has free variables
    i = 0
    while i < len(s):
        if s[i] == LAMBDA:
            term = s[i + 1 : s.find('[', i)]
            close_idx = s.find('[', i) # (λz[z]
            imbalance = 0
            for j in range(close_idx, len(s)):
                if s[j] == '[':
                    imbalance += 1
                elif s[j] == ']':
                    imbalance -= 1
                if not imbalance:
                    close_idx = j
                    break
            if close_idx + 2 >= len(s) or (not s[close_idx + 2].isalnum() and not s[close_idx + 2] == '('):
                s = s[0 : i] + '(' + s[i : close_idx+1] + ")" + term + s[close_idx+1 : ]
                i += 2
        i += 1
    print("s", s)
    stack = []
    # todo: did we ever account for chains like ()()()
    # problem is that order matters, so naive recursion wont work ...
    # what if we process it in the loop after?
    # no, just parse yourself and look inside the stack and update the last element by replacing
    for i in range(0, len(s)):
        if s[i - 1] == ')' and s[i].isalnum():
            stack.pop() # remove )
            stack.pop() # remove ]

            end_arg_idx = i
            while end_arg_idx < len(s) and s[end_arg_idx].isalnum():
                end_arg_idx += 1
            arg = s[i : end_arg_idx]

            # find matching opening bracket
            imbalance = 1 
            curr = ""
            while imbalance:
                if stack[-1] == '(': imbalance -= 1
                elif stack[-1] == ')': imbalance += 1
                if imbalance:
                    curr = stack[-1] + curr
                stack.pop()
            
            lambda_term = curr[1 : curr.find('[')]
            curr = curr[curr.find('[') + 1 :]
            
            stack.append(curr.replace(lambda_term, arg))
        else:
            stack.append(s[i])
    
    if simpl:
        return eval_expr("".join(stack))
    return "".join(stack)