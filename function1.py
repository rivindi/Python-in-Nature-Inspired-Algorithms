#funtion
import math
def calculation():
    print("Python Function");

calculation();

def cal(x):
    #y=f(x)=x^3-5x+3
    y=math.pow(x,3)-5*x+3;
    print(y);
cal(.2);

def calc(x):
    #y=f(x)=x^3-5x+3
    y=math.pow(x,3)-5*x+3;
    return y;
fx=calc(0);
print(fx);
