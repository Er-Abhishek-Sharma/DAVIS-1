n = int(input("Enter your number : "))

for i in range(n):
    for j in range(i):              # spaces
        print(" ", end="")
    for k in range(2*n - (2*i + 1)): # stars
        print("*", end="")
    print()



                 
