from lamb import *

def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)
mark1 = []
print("Average of mark1:",avg(mark1))

val = '(λx[x^2-2*x+5])2'
assert parse(val) == 5
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


