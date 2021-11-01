from turtle import *

n = 7
angle = 360 / n
s_angle = 720 / n

for i in range(n):
    forward(100)
    left(angle)

for i in range(n):
    forward(100)
    left(s_angle)
done()
