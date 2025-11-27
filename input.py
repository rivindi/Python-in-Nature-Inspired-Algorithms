#I/O
import math
def calc(x):
    #y=f(x)=x^3-5x+3
    y=math.pow(x,3)-5*x+3;
    return y;
num1=int(input("Enter an integer to start :"))
num2=int(input("Enter an integer to end :"))
num2=num2+1
list1=[]
for var1 in range(num1,num2):
    list1.append(var1)
list2=[]
for v1 in list1:
    fx=calc(v1);
    #print("X=",v1,"Y =",fx);
    list2.append(fx)
print("X => ",list1)
print("Y => ",list2)
