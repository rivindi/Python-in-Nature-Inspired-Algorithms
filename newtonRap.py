#fx=x^3-2x-5 x0=2
#fx=xsin(x) + cos(x) x0=pi
#x1=x0-f(x0)/f'(x0)
import math
def fun(x):
    fx=math.pow(x,3)-2*x-5
    return fx
def fun1(x):
    #3x^2-2
    fx=3*math.pow(x,2)-2
    return fx
def NewtonRaphson(x):
    #x1=x-(y1/y2)
    y1=fun(x)
    y2=fun1(x)
    x1=x-y1/y2
    return x1
x=2
i=0
while(i<6):
    x=NewtonRaphson(x)
    i=i+1
    print(x)

