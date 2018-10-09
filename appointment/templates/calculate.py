
from sympy import *


x = symbols('x')
answer = solve(LessThan((1-E**(-((x*80)/(1024*x))))**x, (1-E**(-(4*80/1024)))**4), x)
print(answer)
# q = -13.0482400960247/log(-exp(-5/512) + 1)
print(float(-5.26134042253839/log(-exp(-5/64) + 1)))