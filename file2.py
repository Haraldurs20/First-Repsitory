num1 = 1
num2 = 0
num3 = 0
num4 = 0
n = int(input("Enter the length of the sequence: ")) # Do not change this line
for number in range (n):
   
    num1,num2,num3 = num4,num1,num2 
    
    num4 = num1 + num2 + num3
 
    print (num4)