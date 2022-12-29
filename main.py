from lamb import *

# maybe validate parentheses of input too 
val = input("Enter your value: ")

res = parse(val)
if not res:
    print("error")
else:
    print(res)
