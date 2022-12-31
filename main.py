from lamb import *

# print('follows normal order evaluation rules')
# maybe validate parentheses of input too 
val = input("Enter your value:\n")
res = parse(val)
if not res:
    print("error")
else:
    print(res)

# (λx[xx])(λz[zz])


# (λx[(λy[aa])(x)])b => (λx[(λy[xx])])b => λy[bb]
# (λx[(λy[aa])(x)])b => (λx[λy[aa](b)) => λx[bb]