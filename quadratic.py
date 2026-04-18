'''
Quadratic Equation Solver
'''

# Assume values of x
x_values = [-1, 1, 2, 3, 4, 5]
# Coefficients of the quadratic equation ax^2 + bx + c = 0

for x in x_values:
    y = x**2 + 2 * x + 1
    print('x={0}, y={1}'.format(x, y))