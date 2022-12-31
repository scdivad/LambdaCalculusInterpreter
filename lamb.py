from sympy import *

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
LAMBDA = 'λ'

def eval_expr(expression):
    print("sent to eval: " + expression)
    expression = expression.replace('^', '**')
    ret = str(simplify(expression))
    ret = ret.replace('**', '^')
    return ret

def parse_single_expression(s):
    i = s.find(LAMBDA)
    if i == -1: return (None, None)
    # assert i == 2 # todo: make O(1)
    term = s[i + 1 : s.find('[', i)]
    body = s[s.find('[') + 1 : s.rfind(']')]
    return (body, term)

def get_matching_idx(s, lst):
    stack = []
    for i, c in enumerate(s):
        if c == '(' or c == '[':
            stack.append(i)
        elif c == ')' or c == ']':
            lst[stack[-1]] = i
            lst[i] = stack[-1]
            stack.pop()

def format_args_paren(s):
    t = ""
    imbalance = 0
    i = 0
    while i < len(s):
        if s[i].isalnum() and (s[i - 1] == ')' or not i):
            t += '('
            while i < len(s) and s[i].isalnum():
                t += s[i]
                i += 1
            t += ')'
        else:
            t += s[i]
            i += 1
    return t

def parse(s, simpl=False):
    # case where s has free variables
    s = format_args_paren(s)
    print("format 2: ", s)
    # print(s)
    # exit(0)

    matching_idx = [-1] * len(s)
    get_matching_idx(s, matching_idx)

    res = ""
    expressions = []
    stack = []
    i = 0
    while i < len(s):
        # todo: if the lambda on the stack
        # turns out to not have an argument
        # then treat it as if the argument is the term
        

        if s[i] == '(' and (stack and stack[-1] == ')'):
            argument = s[i+1 : matching_idx[i]]

            curr = ")"
            imbalance = 1
            stack.pop()
            while imbalance:
                if stack[-1] == '(': imbalance -= 1
                if stack[-1] == ')': imbalance += 1
                curr = stack.pop() + curr
            
            body, term = parse_single_expression(curr)
            if not body: # could be more efficient
                # is not a lambda expression
                stack.append(curr)
                print("append curr: ", curr)
                stack.append('(')
                for c in argument:
                    stack.append(c)
                stack.append(')')
                i = matching_idx[i] + 1
                continue

            # todo: check if alpha is needed

            # argument and body exist, perform beta
            curr = body.replace(term, argument)
            for c in curr:
                stack.append(c)
            # print(stack)
            # print('end')

            i = matching_idx[i] + 1
        else:
            stack.append(s[i])
            i += 1
    if simpl:
        return eval_expr("".join(stack))
    return "".join(stack)