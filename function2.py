#funtion
import math
def calc(x):
    #y=f(x)=x^3-5x+3
    y=math.pow(x,3)-5*x+3;
    return y;
list1=[-2,-1,0,1,2,3,4]
list2=[]

for v1 in list1:
    fx=calc(v1);
    #print("X=",v1,"Y =",fx);
    list2.append(fx)

print("X => ",list1)
print("Y => ",list2)
