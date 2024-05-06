import numpy as np
x = 0
y = 0

d1, d2, d3 = 0

x1, y1 = 0, 0
x2, y2 = 300, 0 
x3, y3 = 300, 300

def cal_tri(d1, d2, d3):
    scnd = [-2*x2, -2*y2]
    thrd = [-2*x3, -2*y3]
    result = [d2**2 - d1**2 - x2**2 - y2**2, d3**2 - d1**2 - x3**2 - y3**2]
    A = np.array(scnd, thrd)
    B = np.array(result)
    solution = np.linalg.solve(A,B)

    return solution
