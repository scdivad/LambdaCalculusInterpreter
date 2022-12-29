from lamb import *

# maybe validate parentheses of input too 
val = input("Enter your value:\n")
res = parse(val)
if not res:
    print("error")
else:
    print(res)

# (λx[xx])(λz[zz])