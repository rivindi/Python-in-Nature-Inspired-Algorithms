#fx=xsin(x) + cos(x) x0=pi
#x1=x0-f(x0)/f'(x0)
import math
def fun(x):
    fx=x*math.sin(x)+math.cos(x)
    return fx
def fun1(x):
    #xcos(x)
    fx=x*math.cos(x)
    return fx
def NewtonRaphson(x):
    #x1=x-(y1/y2)
    y1=fun(x)
    y2=fun1(x)
    x1=x-y1/y2
    return x1
x=math.pi
i=0
while(i<6):
    x=NewtonRaphson(x)
    i=i+1
    print(x)

