from turtle import *

def detour(L):
    if L < 10:
        forward(10)
    else:
        LL = L/3
        detour(LL)
        left(60)
        detour(LL)
        left(120)
        detour(LL)
        left(60)
        detour(LL)

for i in range(6):
    detour(100)
    left(60)
