# create a program to calculate the simple interest
# create a function that calculate simple interest
def calculate_simple_interest(p, t, r):
    si = (p*t*r)/100
    return si

p = float(input("enter the princple:"))
r = float(input("enter the amount rate:"))
t = int(input("enter the time:"))

simple_interest = calculate_simple_interest(p,t,r)
print(f"Simple interest is: {simple_interest}")


    
