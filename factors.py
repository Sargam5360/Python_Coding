# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input numbers and add those who have exactly three factors. Output the sum

import sys
def print_factors(x):
   # This function takes a number and prints the factors
    count =0
    #print("The factors of",x,"are:")
    for i in range(1, x):
         if x % i == 0:
            #print(i)
            count +=1
            if count > 3:
               return 0
    if count == 3:
        #print count
        return x
    return 0

# change this value for a different result.
num = 3

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

 

#function

for line in sys.stdin:
    #print line
    b = line.split(',')
    x = len(b)
    sum = 0     
for i in range(x):
    a = int(b[i])
    sum += print_factors(a)
    
print sum