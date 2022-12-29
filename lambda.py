from sympy import *

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
lamb = 'λ'

def eval_expr(expression):
    expression = expression.replace('^', '**')
    print("sent to eval: " + expression)
    ret = str(simplify(expression))
    ret = ret.replace('**', '^')
    return ret

def parse(s, simpl=False):
    stack = []
    for i in range(0, len(s)):
        if s[i - 1] == ')' and s[i].isalnum():
            stack.pop() # remove )
            stack.pop() # remove ]

            end_arg_idx = i
            while end_arg_idx < len(s) and s[end_arg_idx].isalnum():
                end_arg_idx += 1
            arg = s[i : end_arg_idx]

            imbalance = 1 # find matching opening bracket
            curr = ""
            while imbalance:
                if stack[-1] == '(':
                    imbalance -= 1
                elif stack[-1] == ')':
                    imbalance += 1
                if imbalance:
                    curr = stack.pop() + curr
                else:
                    stack.pop()
            
            lambda_term = curr[1 : curr.find('[')]
            curr = curr[curr.find('[') + 1 :]
            # print('curr: ', curr)
            # print('x: ', lambda_term)
            # print('arg: ', arg)
            
            stack.append(curr.replace(lambda_term, arg))
        else:
            stack.append(s[i])
    
    if simpl:
        return eval_expr("".join(stack))
    return "".join(stack)

 
# maybe validate parentheses of input too 
val = input("Enter your value: ")
# val = '(lx[x^2-2*x+5])2'
# val = '(λa[(lb[a^2+b^2])b])3'
# val = '(λx[x])y'
# val = '((λx.λy.y)a)b'
# val = '((lx[ly[y]])a)b'
# val = λx([λy([(λz[x(yz)])z)y]])x
# ((lx[ly[y]])a)b
# ([ly[y]])b
# stack solution is the way to go for now
res = parse(val)
if not res:
    print("error")
else:
    print(res)


'''
((λx.λy.y)a)b
(λy.y)b

'''