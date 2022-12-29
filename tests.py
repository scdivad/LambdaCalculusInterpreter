from lamb import *

# val = '(λx[x^2-2*x+5])(2)'
# assert int(parse(val, True)) == 5
# print('TC 0 PASSED')

val = '(λx[x^2-2*x+5])2'
assert int(parse(val, True)) == 5
print('TC 1 PASSED')

val = '(λa[(λb[a^2+b^2])b])3'
assert parse(val) == '3^2+b^2'
print('TC 2 PASSED')

val = '(λx[x])y'
assert parse(val) == 'y'
print('TC 3 PASSED')

val = '((λx[λy[y]])a)b'
assert parse(val) == 'b'
print('TC 4 PASSED')

'''
# 2.2 Combinators 
https://plato.stanford.edu/entries/lambda-calculus/
'''
val = 'λx[λy[λz[xz(yz)]]]'
assert parse(val) == 'xz(yz)'
print('TC 5 PASSED')

val = 'λx[λy[asdf]]'
assert parse(val) == 'asdf'
print('TC 6 PASSED')

val = 'λx[x]'
assert parse(val) == 'x'
print('TC 7 PASSED')

# (λx . λy . y) ¡ (λz . z z) (λz . z z)
# (λx[λy[y]])(λz[zz])(λz[zz]) < todo
# (λx[λy[y]])((λz[zz])(λz[zz])) < todo


# print('curr: ', curr)
# print('x: ', lambda_term)
# print('arg: ', arg)

# print("sent to eval: " + expression)