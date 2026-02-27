import math

r = float(input())
x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())

def dist(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

def angle(a, b):
    return math.atan2(b[1]-a[1], b[0]-a[0])

d0 = math.hypot(x0, y0)
d1 = math.hypot(x1, y1)

if d0 <= r or d1 <= r:
    print("0.0000000000")
else:
    theta0 = math.acos(r/d0)
    theta1 = math.acos(r/d1)
    phi = abs(angle((x0, y0), (x1, y1)))
    delta = math.acos((x0*x1 + y0*y1)/(d0*d1))
    if delta <= theta0 + theta1:
        length = dist((x0, y0), (x1, y1))
    else:
        length = math.sqrt(d0*d0 - r*r) + math.sqrt(d1*d1 - r*r) + r*(delta - theta0 - theta1)
    print(f"{length:.10f}")