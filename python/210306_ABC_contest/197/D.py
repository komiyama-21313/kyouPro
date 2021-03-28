import math
N = int(input())

x0, y0 = map(int, input().split())
xN, yN = map(int, input().split())

xR = (x0 + xN) /2
yR = (y0 + yN) /2

R = ((xR-x0)**2+(yR-y0)**2)**0.5

sitax0 = math.acos((x0-xR)/R)
sitay0 = math.asin((y0-yR)/R)

if y0-yR < 0:
    sitax0 = -1 * sitax0
if x0-xR < 0:
    sitay0 = math.pi - sitay0

cos = math.cos(sitax0 + 2*math.pi/N)
sin = math.sin(sitay0 + 2*math.pi/N)

x1 = xR + R*cos
y1 = yR + R*sin

print(x1, y1)