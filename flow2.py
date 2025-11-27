#Flow control- loop
co=0
while (co<100):
    print(co)
    co=co+1
print("End While")

for var in "Anaconda":
    print(var) #Line by line
print("******")
for var in ["Data Mining","Machine Learning",
            "Maths","Statistics"]:
    print(var)
print("******")
for var in range(1,5):
    print(var)
print("******")    
for var in range(0,101,10):
    print(var)
print("******") 
for var in range(100,-1,-10):
    print(var, end=',')#same line
print()
print("******")
